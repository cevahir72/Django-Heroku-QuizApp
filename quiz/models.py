from django.db import models

# Create your models here.

class Category(models.Model):
    CATEGORY_NAMES = [
        ("Math", "Math"),
        ("Geography", 'Geography'),
        ("History", 'History'),
        ("Literature", 'Literature'),
        ("Science", 'Science'),  
    ]
    
    name= models.CharField(max_length=40 , choices=CATEGORY_NAMES, default="Math")
    
    def __str__(self):
        return self.name

class Quiz(models.Model):
    title = models.CharField(max_length=40)
    createdDate = models.DateTimeField(auto_now_add =True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="quizzes")
    
    def __str__(self):
        return f'{self.category} - {self.title}'
    
    
class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="questions")
    title = models.CharField(max_length=40)
    createdDate = models.DateTimeField(auto_now_add =True)
    updatedDate = models.DateTimeField(auto_now=True)
    
    DIFFICULTY= {
        ("H", "High"),
        ("M", "Medium"),
        ("L", "Low"),
    }  
    difficulty = models.CharField(max_length=50 , choices=DIFFICULTY , default="Low")
    
    def __str__(self):
        return f'{self.quiz} - {self.title}'


class Answer(models.Model):
    updatedDate = models.DateTimeField(auto_now=True)
    createdDate = models.DateTimeField(auto_now_add =True)
    answerText = models.TextField(max_length=200)
    isRight = models.BooleanField( default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE , related_name="answers")
    
    def __str__(self):
        return f'{self.question} - {self.answerText}'
    
    
    
