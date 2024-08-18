from library.extension import db
from library.model import Books, Author, Category, Borrows, Students
from library.library_ma import BookSchema
from flask import request, jsonify
from sqlalchemy.sql import func
import json


def get_borrow_author_cat_service(student_name):
    borrows = db.session.query(Borrows.id, Books.name, Category.name, Author.name).join(
        Students, Borrows.student_id == Students.id).join(Category, Category.id == Books.category_id).join(
        Author, Author.id == Books.author_id).filter(func.lower(Students.name) == student_name.lower()).all
    if borrows:
        return jsonify({f'{student_name} borrowed': borrows}), 200
    else:
        return jsonify({"message": "Not found borrow!"}), 404
