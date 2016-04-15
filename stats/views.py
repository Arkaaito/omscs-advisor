from django.shortcuts import render
from models import EnrollmentSnapshot
from advisor.models import Offering

def dashboard(request):
    summer = {
        "semester_name": "Summer 2016",
        "semester_code": "201605",
        "courses": []
    }
    summer_offerings = Offering.objects.filter(term="Summer2016").all()
    for offering in summer_offerings:
        latest = EnrollmentSnapshot.objects.filter(offering=offering).order_by("-recorded").first()
        prev_offering = Offering.objects.filter(term="Summer2015",course=offering.course).all()
        prev = EnrollmentSnapshot.objects.filter(offering=prev_offering).filter(recorded__year=2015, recorded__month=5, recorded__day=20).order_by("-recorded").first()
        summer["courses"].append({
            "number": offering.course.number,
            "name": offering.course.title,
            "crn": offering.crn,
            "latest": latest,
            "prev": prev
        })
    winter = {
        "semester_name": "Fall 2016",
        "semester_code": "201608",
        "courses": []
    }
    winter_offerings = Offering.objects.filter(term="Winter2016").all()
    for offering in winter_offerings:
        latest = EnrollmentSnapshot.objects.filter(offering=offering).order_by("-recorded").first()
        prev_offering = Offering.objects.filter(term="Winter2015",course=offering.course).all()
        prev = EnrollmentSnapshot.objects.filter(offering=prev_offering).filter(recorded__year=2015, recorded__month=5, recorded__day=22).order_by("-recorded").first()
        winter["courses"].append({
            "number": offering.course.number,
            "name": offering.course.title,
            "crn": offering.crn,
            "latest": latest,
            "prev": prev
        })

    all_stats = [summer, winter]
    return render(request, "dashboard.html", {
        "all_stats": all_stats
    })