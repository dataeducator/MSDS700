---------- DB creation ------------
create database SchoolDB;
use SchoolDB;
-- 
-- Structure de la table teacher
-- 
CREATE TABLE teacher (
  id_teacher smallint(6) NOT NULL auto_increment,
  fname varchar(50) NOT NULL default '',
  lname varchar(50) NOT NULL default '',
  spec enum('Maths','Litt','Hist','Phil') NOT NULL default 'Maths',
  salary mediumint(9) NOT NULL default '0',
  date_recruit date NOT NULL,
  PRIMARY KEY  (id_teacher)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=11;
-- 
-- Contenu de la table teacher
-- 
INSERT INTO teacher VALUES (10,'Ennio','Moricone', 	    'Maths', 	654654, '2002-11-18');
INSERT INTO teacher VALUES (9, 'Ahmed', 'Jundi', 		'Maths', 	654654, '1993-07-21');
INSERT INTO teacher VALUES (8, 'Trando','Grand', 		'Phil', 	6546, 	'1989-02-07');
INSERT INTO teacher VALUES (7, 'Eldo', 	'Martin', 		'Maths', 	1321, 	'1980-12-30');
INSERT INTO teacher VALUES (6, 'Eldo', 	'Malinconi', 	'Maths', 	4565, 	'1995-05-18');
INSERT INTO teacher VALUES (5, 'Geoges','Martin', 		'Litt', 	1321, 	'1991-05-17');
INSERT INTO teacher VALUES (4, 'Manon', 'Lescaut', 		'Hist', 	4654, 	'2002-05-23');
INSERT INTO teacher VALUES (3, 'Yves', 	'Martin', 		'Phil', 	1225, 	'2000-05-25');
INSERT INTO teacher VALUES (2, 'Elodie','Dupont', 		'Litt', 	2055, 	'1987-05-14');
INSERT INTO teacher VALUES (1, 'Smith', 'Dupont', 		'Maths', 	1000, 	'2005-05-18');
--
CREATE TABLE school (
  id_school smallint(6) NOT NULL auto_increment,
  name varchar(50) NOT NULL default '',
  City varchar(50) NOT NULL default '',
  type_sch varchar(7),
  open_year smallint(4),
  PRIMARY KEY  (id_school)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1;
--
INSERT INTO school VALUES (1,'Dearington', 		'Lynchburg', 	'magnet', 1960);
INSERT INTO school VALUES (2,'Montenuru', 		'Lynchburg', 	'private', 1999);
INSERT INTO school VALUES (3,'Sandusky', 		'Lynchburg', 	'private', 2002);
INSERT INTO school VALUES (4,'Robert Monro', 	'Danville', 	'public', 1989);
INSERT INTO school VALUES (5,'Henri Matisse', 	'Blacksburg', 	'private', 2001);
INSERT INTO school VALUES (6,'Charles Meyer', 	'Amherst', 		'public', 1977);
--
CREATE TABLE teaches_at (
  num_sequence smallint(6) NOT NULL auto_increment,
  id_teacher smallint(6) NOT NULL,
  id_school smallint(6) NOT NULL,
  PRIMARY KEY  (num_sequence)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=11;
--
INSERT INTO teaches_at VALUES (1,1,1);
INSERT INTO teaches_at VALUES (2,1,2);
INSERT INTO teaches_at VALUES (3,1,3);
INSERT INTO teaches_at VALUES (4,2,4);
INSERT INTO teaches_at VALUES (5,5,6);
INSERT INTO teaches_at VALUES (6,6,5);
INSERT INTO teaches_at VALUES (7,3,2);
INSERT INTO teaches_at VALUES (8,7,5);
INSERT INTO teaches_at VALUES (9,8,2);
INSERT INTO teaches_at VALUES (10,9,6);
INSERT INTO teaches_at VALUES (11,10,1);
INSERT INTO teaches_at VALUES (12,10,3);