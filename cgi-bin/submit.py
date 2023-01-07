# Import the necessary modules
from cgi import FieldStorage
import csv


# Create a FieldStorage object to hold the form data
form_data = FieldStorage()

# Get the form data
insta = form_data.getvalue("instagram")
email = form_data.getvalue("email")

# Open a file for writing
with open("form_data.csv", "a") as f:
  # Create a CSV writer
  writer = csv.writer(f)
  # Write the form data to the file
  writer.writerow([insta, email])

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Redirecting...</title>"
print "</head>"
print "<body>"

# Redirect to a new page after processing the form
print "<meta http-equiv='refresh' content='0;url=http://127.0.0.1:8080/LandingPage.html'>"

print "</body>"
print "</html>"