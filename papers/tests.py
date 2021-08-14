from django.test import TestCase
from papers.models import ResearchPaper

class Test_Create_Post(TestCase):


    def create_research_paper(self, title="Self Drive",
                              author="Bengio",
                              topic='Self Driving',
                              summary='This paper is about how self driving cars work.'):
        return ResearchPaper.objects.create(
            title=title,
            author=author,
            topic=topic,
            summary=summary
            )
    def test_paper(self):
        paper = self.create_research_paper()
        title = f'{paper.title}'
        author = f'{paper.author}'
        topic = f'{paper.topic}'
        summary = f'{paper.summary}'

        self.assertEqual(title, 'Self Drive')
        self.assertEqual(author,'Bengio' )
        self.assertEqual(topic,'Self Driving' )
        self.assertEqual(summary, 'This paper is about how self driving cars work.')
