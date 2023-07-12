DROP DATABASE IF EXISTS  adopt;

CREATE DATABASE adopt;

\c adopt

CREATE TABLE pets(
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    species TEXT NOT NULL,
    photo_url TEXT,
    age INT,
    notes TEXT,
    available BOOLEAN NOT NULL DEFAULT TRUE
);

INSERT INTO pets
    (name, species, photo_url, age, notes, available)
VALUES
    ('Porky', 'porcupine', 'https://media.istockphoto.com/id/93212051/photo/porcupine.jpg?s=612x612&w=is&k=20&c=22wH2tHnk-LwobXvT8sXKehHbMNhOgb6t05dhD7MvaE=' ),
    ('Cleocatra', 'cat', 'https://media.istockphoto.com/id/1361394182/photo/funny-british-shorthair-cat-portrait-looking-shocked-or-surprised.jpg?s=612x612&w=is&k=20&c=B5GCusry9f4_eF7io_pDGB4cVZ5Itbf9uGaJEGFGXsA='),
    ('Kujo', 'dog', 'https://media.istockphoto.com/id/467923438/photo/silly-dog-tilts-head-in-front-of-barn.jpg?s=612x612&w=is&k=20&c=T5eLQmmzuJkRolskf7RRecXnRHuxyDOEzPnpQaz1nus=');