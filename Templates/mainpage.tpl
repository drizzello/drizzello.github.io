<!DOCTYPE html>
<head>
    <title>Davide's Blog</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style type="text/css">
        body {
            margin: 0 auto;
            padding: 0 auto;
        }

        #wrapper {
            margin: 0 auto;
            max-width: 700px;
            padding: 10px;
        }

        div#page-title {
            display: flex
        }

        a.articleLink {
            text-decoration: none;
            font-style: italic;
        }

        #profile-image-holder {
            width: 100%;    
            padding: 2.5%;
        }

        img#profile-image {
            width: 1.8in;
            border-radius: 50%;
            display: block;
            margin-left: auto;
            margin-right: auto;
        }
        
        span.tag {
            padding: 3px;
            background-color: #F2f2f2;
            border: 1px solid #c2c2c2;
            border-radius: 5px;
            font-size: x-small;
        }

        details > p {
            padding-right: 10px;
            padding-left: 10px;
        }

        #link-logo {
            width: 0.32in;
            height: 0.32in;
        }

        section#links {
            padding: 20px;
            display: flex;
            flex-direction: row;
            justify-content: center;
        }

        a#link {
            margin: 10px;
        }

    </style>
</head>
<body>
    <div id="wrapper">
        <div id="page-title">
            <!-- <div id="profile-image-holder"> -->
            <!--    <img id="profile-image" src="/static/profile.jpg"></img> -->
            <!-- </div> -->
            <p>Hi, I'm Davide, and this is my personal blog where I share my thoughts and experiences.</p>
        </div>
        <div id="content-wrap">
            <details open>
                <summary>ABOUT</summary>
                <p>Developer, Technology Enthusiast, Problem Solver</p>
                <p>I write about various topics in technology, programming, and personal experiences.</p>
                <p>You can find more about me on my social media linked below.</p>
            </details>
            <details>
                <summary>BLOG</summary>
                <section id="article">
                    <ul>
                    {% for a in articles %}
                        <li>
                            <a class="articleLink" href="/article/{{ a.hex_code }}.html">{{ a.title }}</a>
                            {% if a.tags %}
                                {% for t in a.tags %}
                                    <span class='tag'>{{ t }}</span>
                                {% endfor %}
                            {% endif %}
                        </li>
                    {% endfor %} 
                    </ul>
                </section>
            </details>
        </div>
        <div id="footer-link-wrap">
            <section id="links">
                <div id="link-icons">
                    <!-- Update with your own links -->
                    <a id="link" href="https://github.com/drizzello">GitHub</a>
                    <!-- Add more social links as needed -->
                </div>    
            </section>
        </div>
    </div>
</body>
</html>