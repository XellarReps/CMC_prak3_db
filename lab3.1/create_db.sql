CREATE TABLE IF NOT EXISTS public.user_info (
	user_id integer PRIMARY KEY,
	type_user text NOT NULL,
	full_name text NOT NULL,
	faculty text,
	reg_date date NOT NULL,
	email text NOT NULL,
    UNIQUE (email),
    CHECK (email LIKE '_%@_%._%')
);

CREATE TABLE IF NOT EXISTS public.session (
	session_id integer PRIMARY KEY,
	session_info json NOT NULL,
	time_start timestamp without time zone NOT NULL,
	status text NOT NULL,
	time_end time,
	user_id integer REFERENCES user_info ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS public.user_session (
	session_id integer PRIMARY KEY,
	cnt_login_attempts integer NOT NULL,
	actions text[] NOT NULL
);

ALTER TABLE public.user_info DISABLE TRIGGER ALL;
ALTER TABLE public.session DISABLE TRIGGER ALL;
ALTER TABLE public.user_session DISABLE TRIGGER ALL;

BEGIN;

COPY public.user_info FROM '/tmp/db/user_info.csv'
	DELIMITER ','
	CSV;

COPY public.session FROM '/tmp/db/session.csv'
	DELIMITER ','
	CSV;

COPY public.session_info FROM '/tmp/db/session_info.csv'
	DELIMITER ','
	CSV;

COMMIT;

ALTER TABLE public.user_info ENABLE TRIGGER ALL;
ALTER TABLE public.session ENABLE TRIGGER ALL;
ALTER TABLE public.user_session ENABLE TRIGGER ALL;
