import os

def populate():
    python_cat = add_cat('Python', 128, 64)
    
    add_page(cat=python_cat,
        title="Official Python Tutorial",
        url="http://docs.python.org/2/tutorial/", 
        views=1345)
        
    add_page(cat=python_cat,
        title="How To Think Like a Computer Scientist",
        url="http://www.greenteapress.com/thinkpython/",
        views=134)
        
    add_page(cat=python_cat,
        title="Learn Python in 10 Minutes",
        url="http://www.korokithakis.net/tutorials/python/",
        views=276)
        
    django_cat = add_cat("Django", 64, 32)
    
    add_page(cat=django_cat,
        title="Official Django Tutorial",
        url="https://docs.djangoproject.com/en/1.5/intro/tutorial01/",
        views=8976)

    add_page(cat=django_cat,
        title="Django Rocks",
        url="http://www.djangorocks.com/",
        views=1988)
    
    add_page(cat=django_cat,
        title="How to Tango with Django",
        url="http://www.tangowithdjango.com/",
        views=2345)
        
    frame_cat = add_cat("Other Frameworks", 32, 16)
    
    add_page(cat=frame_cat,
        title="Bottle",
        url="http://bottlepy.org/docs/dev/",
        views=6750)
        
    add_page(cat=frame_cat,
        title="Flask",
        url="http://flask.pocoo.org",
        views=7609)
        
    frame_cat = add_cat("Scientific Programming", 16, 8)
    
    add_page(cat=frame_cat,
        title="SciPy",
        url="http://www.scipy.org/",
        views=122)
        
    add_page(cat=frame_cat,
        title="Scientific Computing with Python",
        url="http://www.scientificpython.net",
        views=79)
        
    # Print out what you have added to the end user
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print "- {0} - {1}".format(str(c), str(p))
            
            
def add_page(cat, title, url, views=0):
    # get_or_create() : checks if the entry exists in the database for us. 
    # If it doesn't exist, the method creates it.
    # The [0] at the end of our call to the method to retrieve the object portion 
    # of the tuple returned from get_or_create().
    p = Page.objects.get_or_create(category=cat, title=title, url=url, views=views)[0]
    return p
    
def add_cat(name, views=0, likes=0):
    # The [0] at the end of our call to the method to retrieve the object portion 
    # of the tuple returned from get_or_create().
    c = Category.objects.get_or_create(name=name, views=views, likes=likes)[0]
    
    return c
    
# Start execution here!
if __name__ == '__main__':
    print "Starting Rango population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE',
     'tango_with_django_project.settings')
    from rango.models import Category, Page
    populate()     
    
        
        
        
        
      
