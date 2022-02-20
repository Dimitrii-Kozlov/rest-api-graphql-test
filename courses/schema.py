import graphene
from graphene_django.types import DjangoObjectType
from .models import Course


class CourseType(DjangoObjectType):
    class Meta:
        model = Course


class Query:
    all_courses = graphene.List(CourseType)

    def resolve_all_courses(self, info, **kwargs):
        return Course.objects.all()