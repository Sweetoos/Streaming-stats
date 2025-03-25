# users
- user_id integer unique index primary key
- username text
- email text
- country text
- password_hash text
- child_account bool

# shows_watched
- user_id integer pk
- show_id integer pk

