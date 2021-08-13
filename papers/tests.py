from django.test import TestCase
from papers.models import ResearchPaper

class Test_Create_Post(TestCase):

    @classmethod
    def set_up_test_data(cls):

        research_paper = ResearchPaper.objects.create(
            title='Self Driving Survey',
            author='Bengio',
            topic='Self Driving',
            summary='This paper is about how self driving cars work.'
            )
        research_paper.save()

    def test_paper(self):
        paper = ResearchPaper.postobjects.get(id=1)
        title = f'{paper.title}'
        author = f'{paper.author}'
        topic = f'{paper.topic}'
        summary = f'{paper.summary}'

        self.assertEqual(title, 'Self Driving Survey')
        self.assertEqual(author,'Bengio' )
        self.assertEqual(topic,'Self Driving' )
        self.assertEqual(summary, 'This paper is about how self driving cars work.')
        self.assertEqual(str(paper), 'Self Driving Survey')
