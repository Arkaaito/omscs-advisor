__author__ = 'arkaaito'

from collections import OrderedDict

class Term:
    FIRST = 'Spring2014'
    CURRENT = 'Fall2015'
    HORIZON = 'Spring2022'
    EACH_YEAR = ['Spring', 'Summer', 'Fall']

    @staticmethod
    def range(start_term, end_term, summer=False, all_terms=False):
        allowed_seasons = []
        if summer:
            allowed_seasons = ['Summer']
        elif all_terms:
            allowed_seasons = Term.EACH_YEAR
        else:
            allowed_seasons = ['Spring', 'Fall']
        terms = []
        term = start_term
        year = int(start_term[-4:])
        end_year = int(end_term[-4:])
        while year <= end_year:
            terms.append(term)
            if term == end_term:
                break
            season = term[0:-4]
            year = int(term[-4:])
            season_ind = allowed_seasons.index(season)
            if season_ind + 1 == len(allowed_seasons):
                season = allowed_seasons[0]
                year += 1
            else:
                season = allowed_seasons[season_ind+1]
            term = season + str(year)
        return terms

    @staticmethod
    def min(term1, term2):
        if term1 is None:
            return term2
        else:
            return term1 # TODO

    @staticmethod
    def max(term1, term2):
        if term2 is None:
            return term1
        else:
            return term2 # TODO

    @staticmethod
    def format(term):
        return ' '.join([term[0:-4],term[-4:]])

    @staticmethod
    def valid(term):
        return term[0:-4] in Term.EACH_YEAR # and isinstance(term[-4:], int)

    @staticmethod
    def compare(term1, term2):
        season1 = term1[0:-4]
        year1 = term1[-4:]
        season2 = term2[0:-4]
        year2 = term2[-4:]
        if (year1 < year2) or (year1 == year2 and Term.EACH_YEAR.index(season1) < Term.EACH_YEAR.index(season2)):
            return -1
        elif (year2 < year1) or (year2 == year1 and Term.EACH_YEAR.index(season2) < Term.EACH_YEAR.index(season1)):
            return 1
        else:
            return 0

    @staticmethod
    def compare_keys(item1, item2):
        return Term.compare(item1[0], item2[0])

    @staticmethod
    def sort(terms):
        return sorted(terms, Term.compare)

    @staticmethod
    def sort_keys(terms):
        return OrderedDict(sorted(terms.items(), Term.compare_keys))