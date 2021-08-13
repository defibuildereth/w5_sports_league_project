DROP TABLE games;
DROP TABLE teams;


CREATE TABLE teams (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    manager VARCHAR(255)
);

CREATE TABLE games (
    id SERIAL PRIMARY KEY,
    team_1 INT REFERENCES teams(id),
    team_2 INT REFERENCES teams(id),
    team_1_goals INT,
    team_2_goals INT
);