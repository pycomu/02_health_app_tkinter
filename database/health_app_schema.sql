CREATE TABLE "account" (
	"account_id"	INTEGER,
	"account_name"	TEXT,
	"account_pin"	INTEGER,
	"account_email"	TEXT,
	"account_create_date"	TEXT,
	PRIMARY KEY("account_id" AUTOINCREMENT)
);

CREATE TABLE "child" (
	"child_id"	INTEGER,
	"child_first_name"	TEXT,
	"child_last_name"	TEXT,
	"child_bday"	TEXT,
	"child_gender"	TEXT,
	"child_country"	TEXT,
	"child_create_date"	TEXT,
	"account_id"	INTEGER,
	FOREIGN KEY("account_id") REFERENCES "account"("account_id"),
	PRIMARY KEY("child_id" AUTOINCREMENT)
);

CREATE TABLE "logfile" (
	"logfile_id"	integer,
	"logfile_timestamp"	TEXT,
	"logfile_weight"	REAL,
	"logfile_height"	REAL,
	"logfile_bmi"	REAL,
	"logfile_age_act"	REAL,
	"child_id"	INTEGER,
	FOREIGN KEY("child_id") REFERENCES "child"("user_id"),
	PRIMARY KEY("logfile_id")
);