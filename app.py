from ext import app

if __name__ == "__main__":
    from routes import index, register, search, user, index5, index1, edit_user, delete_user, logout, edit_search, delete_search

    app.run(debug=True)