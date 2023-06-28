import requests
import streamlit as st
from streamlit_lottie import st_lottie
import json

from PIL import Image
from streamlit_card import card



with open('config.json') as cf:
    cfile=json.load(cf)


def navbar():
    st.markdown("""
        <style>
        .navbar {
            display: flex;
            justify-content: space-around;
            background-color: #f5f5f5;
            padding: 10px;
            margin-bottom: 20px;
        }
        .navbar a {
            text-decoration: none;
            color: #333;
            padding: 10px;
            transition: color 0.3s;
        }
        .navbar a:hover {
            color: #ff6600;
        }
        </style>
    
       <div class="navbar">
        <a href="#Experience">Experience</a>
        <a href="#projects">Projects</a>
        <a href="#blogs">Blogs</a>
        <a href="#Tech Stack / Skills">Skills</a>
        <a href="#Publications">Publications</a>
        <a href="#contact">Contact</a>
    </div>""",unsafe_allow_html=True)




def nameandphoto():
    columns=st.columns(2)
    with columns[0]:
        st.title(f" Hi 👋    I am {cfile['name']}")
    with columns[1]:
        st_lottie(lottie_coding, height=200, key="coding")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")

lottie_projects= load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_zP38h7.json")
# Page: Home
def home_page():
    
    st.write("Here you can explore my portfolio, projects, blogs, skills, and contact details.")

    # Add navigation menu
    st.markdown("""
    <style>
        .contact-card {
            background-color: #f5f5f5;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
            transition: box-shadow 0.3s;
            position: relative;
            margin-bottom: 20px;
        }
        .contact-card:hover {
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
        }
        .contact-card-title {
            font-size: 20px;
            margin-bottom: 10px;
        }
        .contact-card-details {
            margin-bottom: 10px;
        }
        .contact-card-icons {
            display: flex;
            justify-content: space-between;
            margin-top: 10px;
        }
        .contact-card-icon {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 40px;
            height: 40px;
            background-color: #333;
            border-radius: 50%;
            margin-right: 10px;
            transition: background-color 0.3s;
        }
        .contact-card-icon img {
            width: 20px;
            height: 20px;
            filter: invert(1);
        }
        .contact-card-icon:hover {
            background-color: #ff6600;
        }
        .col1 {
            font-size: 10px;
        }
        .col2 {
            font-size: 10px;
        }
        
    </style>

    """, unsafe_allow_html=True)

    # Page: Projects
    st.title("Projects")

    columns = st.columns(2)
    # Display top 2 projects
    for project in cfile['projects'][:2]:
        with(columns[0]):
            st.markdown('<div class="project-card">', unsafe_allow_html=True)
            st.write(f"""## {project['title']}""")
            st_lottie(
            load_lottieurl(project['lottie_url']),
            height=500,width=800
        )
            st.write(f"""#### {project['description']} """)
            st.markdown('<div class="project-card-options">', unsafe_allow_html=True)
            st.markdown(f'<a class="project-card-option" href="{project["repository"]}">View Source Code</a> | '
                        f'<a class="project-card-option" href="{project["demo"]}">View Project</a>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

    # "View More" button to show remaining projects
    if len(cfile['projects']) > 2:
        if st.button("View More"):
            for project in cfile['projects'][2:]:
                st.markdown('<div class="project-card">', unsafe_allow_html=True)
                st.image(project['image'], caption=project['description'], use_column_width=True)
                st.markdown(f'<div class="project-card-title">{project["title"]}</div>', unsafe_allow_html=True)
                st.markdown('<div class="project-card-options">', unsafe_allow_html=True)
                st.markdown(f'<a class="project-card-option" href="{project["repository"]}">View Source Code</a> | '
                            f'<a class="project-card-option" href="{project["demo"]}">View Project</a>', unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)

    # Page: Blogs
    st.title("Blogs")

    columns = st.columns(2)
    for blog in cfile['blogs']:
        with columns[0]:
            st.subheader(blog["title"])
            st.write(blog["excerpt"])
            st.write(f"Publication Date: {blog['publication_date']}")
            
        with columns[1]:
            st.image(blog["image_path"], use_column_width=None,width=300)
            st.markdown(f"[Read more]({blog['url']})", unsafe_allow_html=True)



    st.title("Tech Stack / Skills")
    col1, col2 = st.columns(2)
    with col1:
        
        for item in cfile['techstack_skills']:
            st.write(f"### {item['category']}")
            st.write("##### " + ", ".join(item['skills']))

    with col2:
        st_lottie(
            load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_ba013t74.json"),
            height=400,width=400
        )

    # Page: Contact
    st.title("Contact")
    st.write("##### You can reach out to me through the following options:")
    st.markdown(""" 
    <div class="contact-card">
        <div class="contact-card-title">Contact Details</div>
        <div class="contact-card-details">
            Email: keshavbajaj4444@gmail.com
        </div>
        <div class="contact-card-icons">
            <a href="https://www.linkedin.com/yourprofile" class="contact-card-icon">
                <img src="linkedin.png" alt="LinkedIn">
            </a>
            <a href="https://github.com/your_username" class="contact-card-icon">
                <img src="github.png" alt="GitHub">
            </a>
            <a href="https://twitter.com/your_username" class="contact-card-icon">
                <img src="twitter.png" alt="Twitter">
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)


def about_page():
    
    st.title("About")
    
    # About card
    st.markdown('<div class="about-card">', unsafe_allow_html=True)
    
    st.markdown('<div class="about-card-details">', unsafe_allow_html=True)
    st.write(f' ##### {cfile["about"]}', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)



# Main program
def main():
    st.set_page_config(layout="wide",page_title="Keshav Bajaj")  # Set the page title
    navbar()
    nameandphoto()
    about_page()
    # Display the home page content
    home_page()
    hasClicked = card(
    title="My Contact Details",
    text=f"Email:{cfile['email']} ",
    image="http://placekitten.com/200/300",
    url="https://github.com/gamcoh/st-card"
    
)



if __name__ == "__main__":
    main()
