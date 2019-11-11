from flask import render_template


def test():
    return render_template('test.html', name='YUAN')
    return 'Testing'

