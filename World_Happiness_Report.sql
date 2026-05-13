
CREATE TABLE Courses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    course_name VARCHAR(100),`Purchase Date`
    provider VARCHAR(50)
);
INSERT INTO Courses (course_name, provider)
VALUES 
('Google Digital Marketing & E-commerce Professional Certificate', 'Google'),
('Meta Social Media Marketing Professional Certificate', 'Meta'),
('Google Data Analytics Professional Certificate', 'Google'),
('Foundations of Data Science', 'General'),
('Artificial Intelligence for Everyone', 'General');


SELECT * FROM Courses;
SELECT * FROM Courses WHERE provider = 'Google';
