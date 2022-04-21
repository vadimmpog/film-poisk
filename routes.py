from app import app


@app.route('/sign_up', methods=['POST'])
def sign_up():
    """
    Creating new user account
    Args:
        login (string): User's login
        password (string): User's password
        email (string): User's email
        country (string): User's country
    Returns:
        string: Error/Success message
    """
    pass


@app.route('/sign_in', methods=['POST'])
def sign_in():
    """
    Signing in into user's account
    Args:
        login (string): User's login
        password (string): User's password
    Returns:
        string: Error/Success message and user's data into current user's session
    """
    pass


@app.route('/set_sub', methods=['POST'])
def set_sub():
    """
    User sets data about subscriptions
    Args:
        user_id (int): User's id
        cinema_sub (string): Cinema's name
    Returns:
        string: Error/Success message
    """
    pass


@app.route('/search', methods=['POST'])
def search():
    """
    User search film
    Args:
        film_name (string): Searching film/series name
        user_subs ([]string): List of user's subscriptions
    Returns:
        json: Parsing results
    """
    pass
