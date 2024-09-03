# models.py
from neomodel import StructuredNode, StringProperty, FloatProperty, RelationshipTo, RelationshipFrom

class Skill(StructuredNode):
    name = StringProperty(unique_index=True, required=True)

class CurriculumVitae(StructuredNode):
    idCV = StringProperty(unique_index=True, required=True)
    name = StringProperty()
    percentage = FloatProperty()
    skills = RelationshipTo(Skill, 'HAVE')

class JobDescription(StructuredNode):
    idJD = StringProperty(unique_index=True, required=True)
    name = StringProperty()
    skills = RelationshipTo(Skill, 'HAVE')
