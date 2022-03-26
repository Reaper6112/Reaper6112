create database School;
drop table Courses;

CREATE TABLE  Courses
   (	
    ID VARCHAR(6) NOT NULL PRIMARY KEY ,
    Student_ID VARCHAR(6) NOT NULL,
	Course_name VARCHAR(40), 
	City VARCHAR(35), 
	credit FLOAT(10,2)
    #FOREIGN KEY (Student_ID) REFERENCES Students(ID)
	 );

select * from STUDENTS;
select * from COURSES;

INSERT INTO Students VALUES ('A007', 'Ramasundar', 'Bangalore', '0.15', '077-25814763');
INSERT INTO Students VALUES ('A003', 'Alex ', 'London', '0.13', '075-12458969');
INSERT INTO Students VALUES ('A008', 'Alford', 'New York', '0.12', '044-25874365');
INSERT INTO Students VALUES ('A011', 'Ravi Kumar', 'Bangalore', '0.15', '077-45625874');
INSERT INTO Students VALUES ('A010', 'Santakumar', 'Chennai', '0.14', '007-22388644');
INSERT INTO Students VALUES ('A012', 'Lucida', 'San Jose', '0.12', '044-52981425');
INSERT INTO Students VALUES ('A005', 'Anderson', 'Brisban', '0.13', '045-21447739');
INSERT INTO Students VALUES ('A001', 'Subbarao', 'Bangalore', '0.14', '077-12346674');
INSERT INTO Students VALUES ('A002', 'Mukesh', 'Mumbai', '0.11', '029-12358964');
INSERT INTO Students VALUES ('A006', 'McDen', 'London', '0.15', '078-22255588');
INSERT INTO Students VALUES ('A004', 'Ivan', 'Torento', '0.15', '008-22544166');
INSERT INTO Students VALUES ('A009', 'Benjamin', 'Hampshair', '0.11', '008-22536178');

INSERT INTO Courses VALUES ('1','A0001', 'Physics', 'Bangalore', '0.01');
INSERT INTO Courses VALUES ('2','A001', 'Light', 'Bangalore', '0.02');
INSERT INTO Courses VALUES ('3','A001', 'Electricity', 'Bangalore', '0.01');
INSERT INTO Courses VALUES ('4','A001', 'Calculus', 'Bangalore', '0.01');
INSERT INTO Courses VALUES ('5','A001', 'English', 'Bangalore', '0.01');

INSERT INTO Courses VALUES ('6','A012', 'Mathematics', 'Mumbai', '0.01');
INSERT INTO Courses VALUES ('7','A012', 'English', 'Mumbai', '0.01');
INSERT INTO Courses VALUES ('8','A012', 'Science', 'Mumbai', '0.02');
INSERT INTO Courses VALUES ('9','A012', 'Art', 'Mumbai', '0.01');
INSERT INTO Courses VALUES ('10','A012', 'Aerodynamics', 'Mumbai', '0.01');

INSERT INTO Courses VALUES ('11','A008', 'Biology', 'London', '0.02');
INSERT INTO Courses VALUES ('12','A008', 'Chemistry', 'London', '0.01');
INSERT INTO Courses VALUES ('13','A008', 'English', 'London', '0.03');
INSERT INTO Courses VALUES ('14','A008', 'Data Science', 'London', '0.01');

INSERT INTO Courses VALUES ('15','A007', 'Film Intro 101', 'Toronto', '0.01');
INSERT INTO Courses VALUES ('16','A007', 'Acting and Directing', 'Toronto', '0.01');
INSERT INTO Courses VALUES ('17','A007', 'Engineering 101', 'Toronto', '0.02');
INSERT INTO Courses VALUES ('18','A007', 'Advanced Piano', 'Toronto', '0.01');
INSERT INTO Courses VALUES ('19','A007', 'English and Writing', 'Toronto', '0.01');

SELECT S.ID, S.ENAME, C.CREDIT, C.ID, C.COURSE_NAME
FROM Students as S 
RIGHT OUTER JOIN COURSES AS C 
ON S.ID = C.Student_ID;

SELECT S.ID, S.ENAME, C.CREDIT, C.ID, C.COURSE_NAME
FROM Students as S 
LEFT OUTER JOIN COURSES AS C 
ON S.ID = C.Student_ID;

SELECT S.ID, S.ENAME, C.CREDIT, C.ID, C.COURSE_NAME
FROM Students as S 
INNER JOIN COURSES AS C 
ON S.ID = C.Student_ID;