import numpy as np
import math

class MarkSheet:
    def __init__(self, student, course):
        self.student = student
        self.course = course
        self.marks = np.zeros((len(course), len(student)))