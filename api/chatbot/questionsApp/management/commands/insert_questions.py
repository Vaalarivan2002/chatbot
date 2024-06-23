from django.core.management.base import BaseCommand
from questionsApp.models import Question

class Command(BaseCommand):
    help = 'Insert questions and their answers'

    def handle(self, *args, **kwargs):
        question_answers = [
            Question(question="Suitable for beginner or advanced users? ", answer= 'We have courses both for beginners as well as advanced users!'),
            Question(question="Can I learn at my own pace? ", answer= 'Yes, you can extend the duration of the course if you want, but it depends on a specific course. Go through the details for each course for more details.'),
            Question(question="What type of assignment do you give? ", answer= 'Quizzes, written assignments, practical assignments, interactive assignments, coding assignments, multimedia assignments, exams, simulations, and gaming assignments are some of the types of assignments which we provide!'),
            Question(question="What are the pre-requirement for this course? ", answer= 'For beginner level courses, there is no prerequisite. But for advanced courses, you need to have basic level understanding of general programming concepts.'),
            Question(question="How long does this course take to complete? ", answer= 'It depends on individual courses. Most courses are of the duration 6 months to 1 year.'),
            Question(question="How much does the course cost? ", answer= 'Our courses cost from 500INR from 1000INR and varies according to the level of proficiency of the courses.'),
            Question(question="How is the doubt support? ", answer= 'The doubt support is available for 24 hours. If you have any queries, please contact pvaalarivan@gmail.com!'),
            Question(question="Does this course offer placement opportunities also? ", answer= 'No, placement opportunities per se are not provided. However, we do have referral programmes by our mentors!'),
            Question(question="How is the course different from other platform courses? ", answer= 'We have expert-led instruction, comprehensive curriculum,  customized learning pathways, robust support system, networking opportunities, and certification!'),
            Question(question="Is there any money back guarantee if I did not like the course? ", answer= "Yes, we do have a money back guarantee. If you don't like the progamme, you can get your money back upto 1 month of enrolling for the course."),
            Question(question="Is this course relevant in todays market? ", answer= 'Absolutely! This course is in alignment with current industry trends, and the current job market is in a high demand for skills. It also has career advancement opportunities, industry recognition, and covers future-proof skills.'),
            Question(question="Is good DSA a prerequisite for this course? ", answer= 'No DSA is not a prerequisite for beginner courses. However, it is good to have an understanding of basic data structures for advanced courses.'),
            Question(question="How much I can make after completing this course? ", answer= 'Our students get packages upto 40LPA after completing this course.'),
            Question(question="Can I pay in EMI for this course? ", answer= 'Sure, we do have EMI availability for this course. 3-Month Plan: $400 per month (0 interest), 6-Month Plan: $200 per month (0 interest), 12-Month Plan: $100 per month (0 interest)'),
            Question(question="Does this course offer financial aid for under-previleged people? ", answer= 'Yes, we offer financial aid for under-previleged people. We offer upto 50 percent discount provided a valid statement of proof is provided!'),
            Question(question="Does this course offer any certificate? ", answer= 'Yes, we do provide a certificate at the end of the course.'),
            Question(question="Where can I get testimonials for this course? ", answer= 'You can view the testimonials at myEdTechCourse.com/testimonials'),
            Question(question="Who is the mentor for this course? ", answer= 'The mentor for this course is Vaalarivan P, CEO of Google.'),
            Question(question="Is it an online or offline course? ", answer= 'It is an online course!'),
        ]
        Question.objects.bulk_create(question_answers)

        self.stdout.write(self.style.SUCCESS('Successfully inserted questions and answers.'))