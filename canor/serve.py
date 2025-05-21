from livereload import Server, shell

# Define the directory to serve files from (current directory)
server = Server()
server.watch('*.html')  # Watch for changes in HTML files
server.watch('*.css')   # Watch for changes in CSS files
server.watch('*.js')    # Watch for changes in JS files

# Run Python's built-in HTTP server in the background
server.serve(root='.', port=8000)
