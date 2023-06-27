import requests
import streamlit as st
from streamlit_lottie import st_lottie


from PIL import Image

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
        st.title(" Hi 👋    I am Keshav Bajaj")
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
    
    # Display top 2 projects
    projects = [
        {
            "title": "Image-Super-Resolution-Using-Autoencoders-in-Keras/Tensorflow",
            "description": "Conversion of low resolution images to high resolution using autoencoders and keras library with tensorflow as backend\
                Basically This model is trained on most of car images so when you load it it may work better with car images\
                but rather than taking this pretrained weights you can also train it on your own set of images.. You can train it on any dataset you want.",
            "image": "supe.png",
            "repository": "https://github.com/Keshav15/Image-Super-Resolution-Using-Autoencoders-in-Keras",
            "demo": "https://demo.project1.com"
        },
        {
            "title": "Named Entity Recognition using BERT",
            "description": "Description of project 2",
            "image": "hirech.png",
            "repository": "https://github.com/your_username/project2",
            "demo": "https://demo.project2.com"
        },
        # Add more projects as needed
    ]
    columns = st.columns(2)
    # Display top 2 projects
    for project in projects[:2]:
        with(columns[0]):
            st.markdown('<div class="project-card">', unsafe_allow_html=True)
            st.write(f"""## {project['title']}""")
            st_lottie(
            load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_vcvl4urd.json"),
            height=500,width=800
        )
            st.write(f"""#### {project['description']} """)
            st.markdown('<div class="project-card-options">', unsafe_allow_html=True)
            st.markdown(f'<a class="project-card-option" href="{project["repository"]}">View Source Code</a> | '
                        f'<a class="project-card-option" href="{project["demo"]}">View Project</a>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

    # "View More" button to show remaining projects
    if len(projects) > 2:
        if st.button("View More"):
            for project in projects[2:]:
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
    # Display blog posts
    blogs = [
        {
            "title": "Analyzing Decision Tree and K-means Clustering using Iris Dataset",
            "excerpt": "Learn how to analyze decision trees and K-means clustering using the Iris dataset.",
            "publication_date": "2023-05-20",
            "url": "https://www.geeksforgeeks.org/analyzing-decision-tree-and-k-means-clustering-using-iris-dataset/",
            "image_path": "dectre.jpg"
        },
        {
            "title": "Structured vs Unstructured Ward in Hierarchical Clustering using Scikit-learn",
            "excerpt": "Explore the differences between structured and unstructured Ward in hierarchical clustering using Scikit-learn.",
            "publication_date": "2023-05-25",
            "url": "https://www.geeksforgeeks.org/structured-vs-unstructured-ward-in-hierarchical-clustering-using-scikit-learn/",
            "image_path": "hirech.png"
        },
        {
            "title": "Comparing Different Clustering Algorithms on Toy Datasets in Scikit-learn",
            "excerpt": "Compare various clustering algorithms on toy datasets using Scikit-learn.",
            "publication_date": "2023-06-01",
            "url": "https://www.geeksforgeeks.org/comparing-different-clustering-algorithms-on-toy-datasets-in-scikit-learn/",
            "image_path": "diff.png"
        }
    ]

    # Create a grid layout for the blog cards
    columns = st.columns(2)
    for blog in blogs:
        with columns[0]:
            st.subheader(blog["title"])
            st.write(blog["excerpt"])
            st.write(f"Publication Date: {blog['publication_date']}")
            
        with columns[1]:
            st.image(blog["image_path"], use_column_width=None,width=300)
            st.markdown(f"[Read more]({blog['url']})", unsafe_allow_html=True)

    # Page: Skills
    
    st.title("Tech Stack / Skills")
    col1, col2 = st.columns(2)
    with col1:
        
        st.write(
            """
            ### Languages\n
            ##### Python,C++ \n

            ### Frameworks\n
            ##### Tensorflow,Pytorch,Pyspark,Flask, \n

            ### Databases\n
            ##### MySQL, AWS Dynamodb, MongoDB \n

            ### Cloud \n
            ##### AWS, Azure, GCP, \n

            ### Miscellaneous \n
            ##### Machine learning ,Deep learning, NLP, Computer Vision\n 
            ##### AWS lambda, Glue, Beanstalk ,Sagemaker, Git, Github, CI/CD, Docker,K8s
             """
        )

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
    st.write(' ##### I am a passionate software developer with experience in Big Data,cloud and  Machine learning . '
                'My goal is to create meaningful and impactful projects that solve real-world problems. '
                'I am constantly learning and exploring new technologies to expand my skill set and stay up-to-date '
                'with the latest industry trends.', unsafe_allow_html=True)
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



if __name__ == "__main__":
    main()
