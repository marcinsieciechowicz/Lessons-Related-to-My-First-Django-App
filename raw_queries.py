import sqlite3
from my_first_lessons_Django.Question import Question

def main(db_file):
    conn = sqlite3.connect(db_file)
    with conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("select question_text, pub_date from polls_question")
        rows = cur.fetchall()
    list_questions = []
    for row in rows:
        q = Question()
        q.question_text = row["question_text"]
        q.pub_date = row["pub_date"]
        list_questions.append(q)
    print(list_questions)

if __name__ == '__main__':
    main("myfirstsqldb.sqlite")

