@app.route('/user/<int:id>')
def show_id(id):
    return 'id_type:'+type(id)