from django.db import models

# Create your models here.
# định nghĩa class ToDolist,gồm 1 trường tên name
class ToDoList(models.Model):
    name = models.CharField(max_length = 200) #var name,độ dài 200i
                                #same
                                #     #CREATE TABLE myapp_person (
                                #     "id" serial NOT NULL PRIMARY KEY,
                                                                                  #     "name" varchar(30) NOT NULL,
                                #
                                # );

    def _str_(self):
        return self.name
class Item(models.Model):
    todoList = models.ForeignKey(ToDoList,on_delete = models.CASCADE)
    text = models.CharField(max_length = 300)   # độ dài chữ 300
    complete = models.BooleanField()

    def _str_(self):
        return self.text