# Fresh Tomatoes Movies Trailer

This web portal is a Python, Html Based YouTube Movie trailer Platform.
Where for each provided YouTube URL, user will be able to see Tiles for each of the movie.

To Watch a Movie Trailer, user can select/click on a speicifc tile and user can view the trailer by you tube player opening on the portal itself


## Run This Project
Open entertainment_center.py in python shell and then run it with 'F5'. It will re-write and open fresh_tomatoes.html on the browser.


## File Structure
 
fresh_tomatoes.py: This File Consists of All the HTML markup, CSS rules and python methods to invoke tiles content and overwrite file fresh_tomatoes.html

media.py: This FIle has Class 'Movie', which has all the movie related information This Class is ahead used by 'entertainment_center.py' to pass movie related information.

entertainment_center.py: This File imports freshTomatoes to pass on available movie and it imports media to create instance of the Movie class with given parameters.

fresh_tomatoes.html: This File is created dynamically by 'fresh_tomatoes.py', with all the movie trailer contents inside it.
