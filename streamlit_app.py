import requests
import streamlit as st
from streamlit_lottie import st_lottie
import json
import base64
from PIL import Image
from streamlit_card import card
import streamlit.components.v1 as components
import itertools

with open('config.json') as cf:
    cfile = json.load(cf)

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
    </div>""", unsafe_allow_html=True)

def nameandphoto():
    columns = st.columns(2)
    with columns[0]:
        st.title(f" Hi 👋  I am {cfile['name']}")
    with columns[1]:
        st_lottie(lottie_coding, height=200, key="coding")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")

lottie_projects = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_zP38h7.json")

def home_page():
    st.write("Here you can explore my portfolio, projects, blogs, skills, and contact details.")
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

        .experience-card {
            background-color: #f5f5f5;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
            transition: box-shadow 0.3s;
            position: relative;
            margin-bottom: 20px;
        }

        .experience-card img {
            width: 100px;
            height: auto;
            margin-right: 20px;
        }

        .experience-card h3 {
            margin-top: 0;
            margin-bottom: 10px;
        }

        .experience-card h4 {
            margin: 0;
        }

        .experience-card p {
            margin-top: 10px;
        }

    </style>
    """, unsafe_allow_html=True)
    
    st.title("Work Experience")

    for experience in cfile['work_experience']:
        st.markdown('<div class="experience-card">', unsafe_allow_html=True)

        if experience.get('company_logo'):
            st.image(experience['company_logo'], width=100)

        st.write(f"## {experience['company_name']}")
        st.write(f"### {experience['start_date']} - {experience['end_date']}")
        st.write(f"#### {experience['job_title']}")
        st.write(experience['job_description'])

        st.markdown('</div>', unsafe_allow_html=True)

    st.title("Projects")
    projects = cfile['projects']
    project_pairs = itertools.zip_longest(*[iter(projects)] * 2)

    columns = st.columns(2)
    card_template = """
    <div class="custom-card">
        <h3>{title}</h3>
        <img src="{image_url}" alt="{title} Image" style="width: 200px; height: 200px; object-fit: cover; border-radius: 10px;">
        <p>{description}</p>
        <div class="card-links">
            <a class="card-link" href="{repository}" target="_blank">View Source Code</a>
            <a class="card-link" href="{demo}" target="_blank">View Project</a>
        </div>
    </div>
    """

    css_styles = """
    <style>
    .custom-card {
        border: 1px solid #ddd;
        border-radius: 10px;
        padding: 20px;
        transition: box-shadow 0.3s;
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
    }

    .custom-card:hover {
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
    }

    .card-content p {
        margin-bottom: 20px;
    }

    .card-links {
        display: flex;
        justify-content: center;
    }

    .card-link {
        display: inline-block;
        margin: 0 10px;
        padding: 8px 16px;
        background-color: #f5f5f5;
        color: #333;
        text-decoration: none;
        border-radius: 5px;
        transition: background-color 0.3s;
    }

    .card-link:hover {
        background-color: #ff6600;
        color: #fff;
    }
    </style>
    """

    st.markdown(css_styles, unsafe_allow_html=True)
    for project1, project2 in project_pairs:
        columns = st.columns(2)

        with columns[0]:
            if project1:
                st.markdown(card_template.format(
                    title=project1["title"],
                    image_url=project1.get("image", ""),
                    description=project1["description"],
                    repository=project1["repository"],
                    demo=project1["demo"]
                ), unsafe_allow_html=True)

        with columns[1]:
            if project2:
                st.markdown(card_template.format(
                    title=project2["title"],
                    image_url=project2.get("image", ""),
                    description=project2["description"],
                    repository=project2["repository"],
                    demo=project2["demo"]
                ), unsafe_allow_html=True)

    st.title("Blogs")
    blogs = cfile['blogs']
    blog_pairs = itertools.zip_longest(*[iter(blogs)] * 2)
    
    for blog1, blog2 in blog_pairs:
        columns = st.columns(2)

        with columns[0]:
            if blog1:
                card1 = card(
                    title=f"{blog1['title']}",
                    text=f"{blog1['excerpt']}",
                    image=f'{blog1.get("image_path", "")}',
                    styles={
                        "card": {
                            "width": "600px",
                            "height": "200px",
                            "border-radius": "10px",
                            "box-shadow": "0 0 10px rgba(0,0,0,0.5)",
                            "margin": "10px",
                            "padding": "10px"
                        },
                        "text": {
                            "font-family": "serif"
                        }
                    },
                    url=f"{blog1['url']}",
                    on_click=lambda: print("Clicked!")
                )

        with columns[1]:
            if blog2:
                card2 = card(
                    title=f"{blog2['title']}",
                    text=f"{blog2['excerpt']}",
                    image=f'{blog2.get("image_path", "")}',
                    styles={
                        "card": {
                            "width": "600px",
                            "height": "200px",
                            "border-radius": "10px",
                            "box-shadow": "0 0 10px rgba(0,0,0,0.5)",
                            "margin": "10px",
                            "padding": "10px"
                        },
                        "text": {
                            "font-family": "serif"
                        }
                    },
                    url=f"{blog2['url']}",
                    on_click=lambda: print("Clicked!")
                )

    st.title("Tech Stack / Skills")
    col1, col2 = st.columns(2)
    with col1:
        for item in cfile['techstack_skills']:
            st.write(f"### {item['category']}")
            st.write("##### " + ", ".join(item['skills']))

    with col2:
        st_lottie(
            load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_ba013t74.json"),
            height=400, width=400
        )

    st.title("Contact")
    st.write("##### You can reach out to me through the following options:")
    st.markdown('<div class="contact-card">', unsafe_allow_html=True)
    st.markdown('<div class="contact-card-title"><h3>Contact Details</h3></div>', unsafe_allow_html=True)
    st.markdown('<div class="contact-card-details"><h4>Email: keshavbajaj4444@gmail.com</h4></div>', unsafe_allow_html=True)

    columns = st.columns(3)

    with columns[0]:
        res = card(
            title="",
            text="",
            image="https://w7.pngwing.com/pngs/585/671/png-transparent-linkedin-communication-linkedin-corporation-corporation-3d-linkedin-3d-linkedin-logo-3d-icon-thumbnail.png",
            styles={
                "card": {
                    "width": "100px",
                    "height": "100px",
                    "border-radius": "60px",
                    "box-shadow": "0 0 10px rgba(0,0,0,0.5)", 
                },
                "text": {
                    "font-family": "serif", 
                }
            },
            url=f"{cfile['social_links'].get('linkedin_url', '')}",
            on_click=lambda: print("Clicked!")
        )

    with columns[1]:
        res2 = card(
            title="",
            text="",
            image="https://1000logos.net/wp-content/uploads/2021/05/GitHub-logo-500x281.png",
            styles={
                "card": {
                    "width": "100px",
                    "height": "100px",
                    "border-radius": "60px",
                    "box-shadow": "0 0 10px rgba(0,0,0,0.5)", 
                },
                "text": {
                    "font-family": "serif", 
                }
            },
            url=f"{cfile['social_links'].get('github_url', '')}",
            on_click=lambda: print("Clicked!")
        )

    with columns[2]:
        res3 = card(
            title="",
            text="",
            image="https://www.seekpng.com/png/full/15-155124_twitter-creative-icon-twitter-twitter-icon-twiter-twitter.png",
            styles={
                "card": {
                    "width": "100px",
                    "height": "100px",
                    "border-radius": "60px",
                    "box-shadow": "0 0 10px rgba(0,0,0,0.5)", 
                },
                "text": {
                    "font-family": "serif", 
                }
            },
            url=f"{cfile['social_links'].get('twitter_url', '')}",
            on_click=lambda: print("Clicked!")
        )
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

def about_page():
    st.title("About")
    st.markdown('<div class="about-card">', unsafe_allow_html=True)
    st.markdown('<div class="about-card-details">', unsafe_allow_html=True)
    st.write(f'##### {cfile["about"]}', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

def main():
    st.set_page_config(layout="wide", page_title="Keshav Bajaj")
    navbar()
    nameandphoto()
    about_page()
    home_page()

if __name__ == "__main__":
    main()
