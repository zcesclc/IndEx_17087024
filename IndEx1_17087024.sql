/*
Write queries to answer the following questions
Save your work to this .sql file
Right click on the file name in the Project pane and select Refactor > Rename, and replace STU_NUM with your student number.
*/

--1. Which employees have 'IT' in their job title? (list their EmployeeId, FirstName, LastName and Title)
SELECT EmployeeId, Firstname, Lastname, Title
from Employee
WHERE Title LIKE "IT%";

--2. List the names of all Artists and the titles of their albums
SELECT Artist.Name, A.title FROM Artist JOIN Album A on Artist.ArtistId = A.ArtistId

--3. Which track is features on the greatest number of times in playlists and how many times is it included? (List track name and the total number of appearances in playlists)
SELECT Track.Name, count(*) from Track JOIN PlaylistTrack PT on Track.TrackId = PT.TrackId
JOIN Playlist P on PT.PlaylistId = P.PlaylistId
GROUP BY Track.TrackId
ORDER BY count(*) DESC

--4. Provide a list of the number of tracks by each artist
SELECT Artist.Name, COUNT(T.TrackId) FROM Artist JOIN Album A on Artist.ArtistId = A.ArtistId
JOIN Track T on A.AlbumId = T.AlbumId
GROUP BY Artist.Name


--5. How much money has been invoiced for the artist Deep Purple? (display each line item from the invoices and the total amount)
SELECT  SUM (I.Total)
FROM Invoice I JOIN InvoiceLine L on L.InvoiceId = I.InvoiceId
JOIN Track T on L.TrackId = T.TrackId
JOIN Album A on T.AlbumId = A.AlbumId
JOIN Artist A2 on A.ArtistId = A2.ArtistId
WHERE A2.name = 'Deep Purple'
