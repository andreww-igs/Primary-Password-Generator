SELECT Surname, Forename, Preferred, Login, StudentEmailAddress, '' AS Password, YearGroup, FormName AS Class
FROM vStudents
-- WHERE YearGroupCode = 'Y06'
WHERE YearGroupCode IN ('KG', 'Y01', 'Y02', 'Y03', 'Y04', 'Y05', 'Y06')
ORDER BY YearGroupCode, FormName, StudentEmailAddress;