from collections import OrderedDict
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth import login

from advisor.config import Term
from advisor.forms import ReviewForm
from advisor.models import Course, Offering, Specialization, Review, Plan, Profile

import logging
logger = logging.getLogger(__name__)

def home(request):
    return redirect('login')

def course_metadata(request):
    terms = Term.range(Term.CURRENT, Term.HORIZON, all_terms=True)
    offerings_by_term = OrderedDict()
    for term in terms:
        offerings_by_term[term] = Offering.objects.filter(term=term).order_by("-average_value").all()
    return render(request, "meta/courses.html", {
        'terms': offerings_by_term,
        'test': (offerings_by_term['Fall2015'])
    })

def specialization_metadata(request):
    return render(request, "meta/specializations.html", {
        'specializations': Specialization.objects.all()
    })

@login_required(login_url='/login/')
def planner(request):
    completed_courses = []
    plan = None
    if request.user != None:
        completed_courses = Review.objects.filter(user=request.user).all()
        try:
            plan = request.user.plans.all()
        except Plan.DoesNotExist:
            plan = None
        def sort_plans(plan1, plan2):
            return Term.compare(plan1.target_term, plan2.target_term)
        plan = sorted(plan, sort_plans)

    return render(request, "planner.html", {
        'plan': plan,
        'completed_courses': completed_courses
    })

def browse_courses(request, term=Term.CURRENT):
    courses = Offering.objects.filter(term=term).order_by("-average_value").all()
    return render(request, "courses/index.html", {
        'courses': courses,
        'term': term
    })

def view_course(request, id, offering=None):
    # TODO: remove me after resetting database
    for user in User.objects.all():
        try:
            has_profile = (user.profile is not None)
        except Profile.DoesNotExist:
            Profile.objects.create(user=user)

    course = Course.objects.get(id=id)
    if offering is None:
        try:
            offering = Offering.objects.get(course=course, term=Term.CURRENT)
        except Offering.DoesNotExist:
            offering = Offering.objects.filter(course=course).order_by('term').first()
    else:
        offering = Offering.objects.get(course=course, id=offering)
    # TODO: error out if bad id / offering
    friends_in_course = []
    if request.user is not None:
        friends = request.user.profile.friends.all()
        for friend in friends:
            if friend.profile.plans.filter(offering=offering).exists():
                friends_in_course.append(friend)


    reviews = Review.objects.filter(offering__course=course).all()
    return render(request, "courses/view.html", {
        'course': course,
        'offering': offering,
        'reviews': reviews,
        'friends': friends_in_course
    })

# Something of a misnomer - really the review is associated with a particular offering.
@login_required(login_url='/login/')
def review_course(request, id):
    course = Course.objects.get(id=id)
    form = ReviewForm()
    instance = None
    offerings = Offering.objects.filter(course=course,term__in=Term.range(Term.FIRST, Term.CURRENT, all_terms=True))
    if Review.objects.filter(offering__in=offerings,user=request.user).exists():
        instance = Review.objects.get(offering__in=offerings, user=request.user)
    form = ReviewForm(instance=instance)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=instance)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return HttpResponseRedirect("/profile/history")
    form.fields["offering"].queryset = offerings
    return render(request, "courses/review.html", {
        'course': course,
        'offerings': offerings,
        'form': form
    })

def get_viewed_user(viewer, id=None):
    # TODO: permissions checking
    if id is not None:
        return User.objects.get(id=id)
    else:
        return viewer

@login_required(login_url='/login/')
def profile_info(request, viewed=None):
    viewed_user = get_viewed_user(request.user, viewed)
    if request.user == viewed_user:
        return render(request, "profile/edit_info.html", {
            'viewer': request.user,
            'viewee': viewed_user
        })
    else:
        return render(request, "profile/info.html", {
            'viewer': request.user,
            'viewee': viewed_user
        })

@login_required(login_url='/login/')
def profile_plan(request, viewed=None):
    if request.method == "POST":
        Plan.objects.filter(user=request.user).delete()
        for term in request.POST:
            courses = request.POST.getlist(term)
            term = term[0:-2]
            if Term.valid(term):
                try:
                    term_plan = Plan.objects.get(user=request.user, target_term=term)
                    term_plan.offerings.clear()
                except Plan.DoesNotExist:
                    term_plan = Plan(user=request.user, target_term=term)
                    term_plan.save()
                for course_key in courses:
                    course = Course.objects.get(key=course_key)
                    offering = Offering.objects.get(course=course, term=term)
                    term_plan.offerings.add(offering)

    viewed_user = get_viewed_user(request.user, viewed)
    show_edit = (request.user == viewed_user)
    plan = None
    try:
        plan = viewed_user.plans.all()
    except Plan.DoesNotExist:
        plan = None

    def sort_plans(plan1, plan2):
        return Term.compare(plan1.target_term, plan2.target_term)

    return render(request, "profile/plan.html", {
        'viewer': request.user,
        'viewee': viewed_user,
        'plan': sorted(plan, sort_plans),
        'can_edit': show_edit
    })

@login_required(login_url='/login/')
def profile_follow(request, followed=None):
    followed_user = get_viewed_user(request.user, followed)
    if (request.user == followed_user):
        # No user provided - error out
        return {}
    return request.user.profile.friends.add(followed_user)

@login_required(login_url='/login/')
def profile_history(request, viewed=None):
    viewed_user = get_viewed_user(request.user, viewed)
    history = {}
    for review in Review.objects.filter(user=viewed_user).all():
        if review.offering.term not in history:
            history[review.offering.term] = []
        history[review.offering.term].append(review)
    show_edit = (request.user == viewed_user)
    return render(request, "profile/history.html", {
        'viewer': request.user,
        'viewee': viewed_user,
        'history': OrderedDict(sorted(history.items(), Term.compare_keys)),
        'can_edit': show_edit
    })

@login_required(login_url='/login/')
def account(request):
    return render(request, "profile/edit_account.html", {
        'user': request.user
    })

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return HttpResponseRedirect("/courses/")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {
        'form': form,
    })