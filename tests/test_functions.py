# from flask_sqlalchemy import SQLAlchemy
# from flaskbasic.wsgi import *
from src.flaskbasic.functions import Functions
import pytest

fun = Functions

def test_student_name():
    assert fun.readName('Lwando',1) == 'Lwando'
    assert fun.readName('Zukisa',2) == 'Zukisa'
    assert fun.readName('ludwe',3) == 'ludwe'

def test_all_results():
    assert fun.readResults(1, 'Lwando',10,60,10) == (1, 'Lwando', 10, 60, 10)

    
    
	

		