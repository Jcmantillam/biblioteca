# biblioteca
Proyecto en python django para buscar y almacenar información, permitiendo la consulta a los APIs de Google books y Oreilly

#Instalación
Se descarga el proyecto, y se va a la ubicación del direcotrio principal, se utilizan los siguientes comandos:
```
git clone https://github.com/Jcmantillam/biblioteca.git
cd biblioteca
pip install -r requirements.txt
python manage.py migrate
```
#Servicios
Los servicios principales son el de búsqueda, guardar un libro y eliminar un libro. Adicionalmente, se puede utilizar le servicio ofrecido por Django Rest framework consultar los libros guardados, o crear un super usuario para Django Admin.  A continuación se explica cada servicio:

**Search Book**
Este servicio permite buscar información de libros tanto en la BD local, como en los servicios externos soportados `GoogleBooks` y `Oreilly`
----
  <Retorna un json con los resultado encontrados, si no hay datos en la BD local, busca en el servicio alternativo indicado>
 
 * **URL**

  <api/v1/search_book/>
 
 * **Método:**
  `GET`

* **Parámetros de datos**
**Requeridos:**
  `search_term=[String]`
  `alternative_service:[Char]`
 <`search_term` es el término buscado, mientras que `alternative_service` determina qué API externa se usará, G para Google y O para O'reilly>

* **Respuesta:**
  
  <Local>
  * **Code:** 200 <br />
    **Content:** `
  [
    {
        "id": 5,
        "title": "Python machine learning",
        "subtitle": "aprendizaje automático y aprendizaje profundo con Python, scikit-learn y TensorFlow",
        "release_date": "2019-01-01",
        "image": null,
        "description": "Not found",
        "editor": 5,
        "authors": [
            8,
            9
        ],
        "categories": [
            17
        ],
        "service": "local"
    }
  ]
  
  `
 
  <Google>
  * **Code:** 200 <br />
    **Content:** `
    {
    "kind": "books#volumes",
    "totalItems": 522,
    "items": [
        {
            "kind": "books#volume",
            "id": "c6a2wgEACAAJ",
            "etag": "TPW/jYQQw4M",
            "selfLink": "https://www.googleapis.com/books/v1/volumes/c6a2wgEACAAJ",
            "volumeInfo": {
                "title": "Python Machine Learning: Aprendizaje automático y aprendizaje profundo con Python, scikit-learn y TesnorFlow",
                "industryIdentifiers": [
                    {
                        "type": "ISBN_10",
                        "identifier": "8426727204"
                    },
                    {
                        "type": "ISBN_13",
                        "identifier": "9788426727206"
                    }
                ],
                "readingModes": {
                    "text": false,
                    "image": false
                },
                "pageCount": 618,
                "printType": "BOOK",
                "maturityRating": "NOT_MATURE",
                "allowAnonLogging": false,
                "contentVersion": "preview-1.0.0",
                "panelizationSummary": {
                    "containsEpubBubbles": false,
                    "containsImageBubbles": false
                },
                "language": "es",
                "previewLink": "http://books.google.com.co/books?id=c6a2wgEACAAJ&dq=Python&hl=&cd=1&source=gbs_api",
                "infoLink": "http://books.google.com.co/books?id=c6a2wgEACAAJ&dq=Python&hl=&source=gbs_api",
                "canonicalVolumeLink": "https://books.google.com/books/about/Python_Machine_Learning_Aprendizaje_auto.html?hl=&id=c6a2wgEACAAJ"
            },
            "saleInfo": {
                "country": "CO",
                "saleability": "NOT_FOR_SALE",
                "isEbook": false
            },
            "accessInfo": {
                "country": "CO",
                "viewability": "NO_PAGES",
                "embeddable": false,
                "publicDomain": false,
                "textToSpeechPermission": "ALLOWED",
                "epub": {
                    "isAvailable": false
                },
                "pdf": {
                    "isAvailable": false
                },
                "webReaderLink": "http://play.google.com/books/reader?id=c6a2wgEACAAJ&hl=&printsec=frontcover&source=gbs_api",
                "accessViewStatus": "NONE",
                "quoteSharingAllowed": false
            },
            "save_link": "http://localhost:8000/api/v1/save_book/?book_id_g=c6a2wgEACAAJ"
        }
    ],
    "service": "G"
    `

  <Oreilly>
  * **Code:** 200 <br />
    **Content:** `
    {
    "results": [
        {
            "id": "https://www.safaribooksonline.com/api/v1/book/9780135917411/",
            "archive_id": "9780135917411",
            "ourn": "urn:orm:video:9780135917411",
            "last_modified_time": "2020-08-20T15:47:56.431Z",
            "issued": "2019-08-26T00:00:00Z",
            "format": "video",
            "content_format": "video",
            "authors": [
                "Paul J. Deitel"
            ],
            "publishers": [
                "Pearson"
            ],
            "academic_excluded": false,
            "language": "en",
            "title": "Python Fundamentals",
            "url": "https://learning.oreilly.com/api/v1/book/9780135917411/",
            "web_url": "/videos/python-fundamentals/9780135917411/",
            "source": "application/epub+zip",
            "content_type": "book",
            "duration_seconds": 162910,
            "video_classification": "course",
            "has_assessment": false,
            "timestamp": "2021-06-02T23:20:46.773Z",
            "description": "<span><p><strong>51+ hours of video instruction</strong>.</p><p><strong>Overview</strong></p><p>The professional programmer’s Deitel® video guide to Python development with the powerful IPython and Jupyter Notebooks platforms.</p><p><strong>Description</strong></p><p>Python Fundamentals LiveLessons with Paul Deitel is a code-oriented presentation of Python—one of the world’s most popular and fastest growing languages. In the context of scores of real-world code examples ranging from individual snippets to complete scripts, Paul will demonstrate coding with the interactive IPython interpreter and Jupyter Notebooks. You’ll quickly become familiar with the Python language, its popular programming idioms, key Python Standard Library modules and several popular open-source libraries. In the Intro to Data Science videos, Paul lays the groundwork for later lessons in which he’ll introduce some of today’s most compelling, leading-edge computing technologies, including natural language processing, data mining Twitter® for sentiment analysis, cognitive computing with IBM® Watson™, supervised machine learning with classification and regression, unsupervised machine learning with clustering, computer vision through deep learning and convolutional neural networks, sentiment analysis through deep learning with recurrent neural networks, big data with Hadoop®, Spark™ streaming, NoSQL databases and the Internet of Things.</p><p>Download the code examples for this LiveLesson from <a href=\"https://github.com/pdeitel/PythonFundamentalsLiveLessons\" target=\"_blank\">https://github.com/pdeitel/PythonFundamentalsLiveLessons</a>. This repository will be updated with the additional lessons’ examples as the lessons are completed.</p><p><strong>About the Instructor</strong></p><p><strong>Paul J. Deitel</strong>, CEO and Chief Technical Officer of Deitel &amp; Associates, Inc., is a graduate of MIT, where he studied Information Technology. He holds the Sun (now Oracle) Certified Java Programmer and Certified Java Developer certifications, and is an Oracle Java Champion. Through Deitel &amp; Associates, Inc., he has delivered Java, C#, Visual Basic, C++, C and Internet programming courses to industry clients, including Cisco, IBM, Sun Micro systems, Dell, Siemens, Lucent Technologies, Fidelity, NASA at the Kennedy Space Center, the National Severe Storm Laboratory, White Sands Missile Range, Rogue Wave Software, Boeing, SunGard Higher Education, Stratus, Cambridge Technology Partners, One Wave, Hyperion Software, Adra Systems, Entergy, CableData Systems, Nortel Networks, Puma, iRobot, Invensys and many more. He and his co-author, Dr. Harvey M. Deitel, are the world’s best-selling programming-language textbook/professional book authors.</p><p><strong>Skill Level </strong></p><p>Beginner-to-Intermediate</p><p><strong>What you Will Learn in Part I</strong></p><ul><li>Before You Begin—Configure your system for Python, obtain the code examples, Python package managers, Paul’s contact info </li><li>Lesson 1—Test-Drives: Using IPython and Jupyter Notebooks—Work with snippets and scripts in the context of IPython and Jupyter Notebooks</li><li>Lesson 2—Intro to Python Programming—Variables, types, operators, strings, I/O, decisions, objects and dynamic typing<br/>\n</li><li>Lesson 3—Control Statements—if, if…else, if…elif…else, for, while, break, continue, augmented assignments, boolean operators, intro to lists</li><li>Lesson 4—Functions—Custom function definitions, importing libraries, simulation with random-number generation, scope, default parameter values, keyword arguments, arbitrary argument lists, methods, intro to tuples, intro to functional-style programming</li></ul><p><strong>What you will learn in Part II:</strong></p><ul><li>Lesson 5—Sequences: Lists and Tuples—Create, initialize and access the elements of lists and tuples; sort and search lists, and search tuples; pass lists and tuples to functions and methods; list methods; functional-style programming (lambdas, filter, map, reduce, list comprehensions, generator expressions, 2D lists); static visualization with the Seaborn and Matplotlib visualization libraries.</li><li>Lesson 6—Dictionaries and Sets—Dictionaries of key—value pairs; sets of unique values; iterating through keys, values and key—value pairs; adding, removing and updating key—value pairs; dictionary and set comparison operators; set operators and methods; operators <strong>in</strong> and <strong>not</strong> <strong>in</strong> for membership testing; mutable set operations; dictionary and set comprehensions; dynamic visualization with the Seaborn and Matplotlib visualization libraries.</li><li>Lesson 7—Array-Oriented Programming with NumPy—<strong>numpy</strong> module’s high-performance <strong>ndarray</strong>s; how <strong>ndarray</strong>s differ from lists; comparing list vs. <strong>ndarray</strong>performance with the IPython <strong>%timeit</strong> magic; one-dimensional and multidimensional<strong>ndarray</strong>s; common <strong>ndarray</strong> manipulations; introduction to the pandas data manipulation library; one-dimensional <strong>Series</strong> and two-dimensional <strong>DataFrame</strong>s; custom <strong>Series</strong> and <strong>DataFrame</strong> indices; basic descriptive statistics for data in a<strong>Series</strong> and a <strong>DataFrame</strong>; customizing pandas output formatting.</li></ul><p><strong>What you will learn in Part III:</strong></p><ul><li>Lesson 8—Strings: A Deeper Look—String methods; string formatting; concatenating and repeating strings; stripping whitespace; string comparisons; search strings for substrings and replacing substrings; tokenizing strings; regular expressions for pattern matching, replacing substrings and validating data; manipulating data in pandas.</li><li>Lesson 9—Files and Exceptions—Text-file processing; serializing objects into the JSON with the <strong>json</strong> module; <strong>with</strong> statement for avoiding “resource leaks”; exception handling; <strong>try</strong>…<strong>except</strong> statement; <strong>else</strong> clause; executing code when no exceptions occur in a <strong>try</strong> suite; <strong>finally</strong> clause; <strong>raise</strong> exceptions; more details on tracebacks; stack unwinding; CSV file processing via the <strong>csv</strong> module; loading and manipulating CSV files in pandas.</li><li>Lesson 10—Object-Oriented Programming—Custom classes; controlling access to attributes; properties for data access; simulating “private” attributes; Python special methods for customizing string representations; inheritance, duck typing and polymorphism; class <strong>object</strong>; Python special methods for overloading operators; named tuples; Python 3.7 data classes; unit testing with <strong>doctest</strong>; namespaces and how they affect scope; Introduction to time series and simple linear regression.</li></ul><p><strong>What you will learn in Part IV:</strong></p><ul><li>Lesson 11—Natural Language Processing (NLP)—Install and use the TextBlob, NLTK, Textatistic and spaCy NLP libraries;, tokenize text into words and sentences; parts-of-speech tagging (noun, verb, etc.); sentiment analysis (positive, negative or neutral); detect the language of text; translate between languages; get word roots via stemming and lemmatization; spell checking and correction; word definitions, synonyms and antonyms; remove stop words from text; create word-cloud visualizations; determine text readability.</li><li>Lesson 12—Data Mining Twitter®—Access tweets and other information on Twitter with Tweepy—a popular Python Twitter API client; search past tweets with the Twitter Search API; sample the live tweet stream with the Twitter Streaming API; work with tweet object meta data; use NLP techniques to clean and preprocess tweets for analysis; perform sentiment analysis on tweets; spot trending topics with Twitter’s Trends API; map tweets using folium and OpenStreetMap.</li><li>Lesson 13—IBM Watson® and Cognitive Computing—Intro to Watson and its free Lite tier services; demos of several Watson services; registering for an IBM Cloud account; set up and get credentials for Watson services; install the Watson Developer Cloud Python SDK; build a Traveler’s companion language translator app that mashes up the Watson Speech to Text, Language Translator and Text to Speech services.</li></ul><p><strong>What you will learn in Part V’s case studies:</strong></p><ul><li><strong>Lesson 14—</strong><strong>Machine Learning: Classification, Regression and Clustering</strong>—Use <strong>scikit-learn</strong> with <strong>popular datasets</strong> to perform machine learning studies; Use Seaborn and Matplotlib to <strong>visualize and explore data</strong>; Perform <strong>supervised machine learning</strong> with <strong>k-nearest neighbors classification</strong> and <strong>linear regression</strong>; Perform <strong>multi-classification</strong> with <strong>Digits dataset</strong>; Divide a dataset into <strong>training</strong>, <strong>testing</strong> and <strong>validation sets</strong>; <strong>Tune hyperparameters</strong> with <strong>k-fold cross-validation</strong>; Measure <strong>model performance</strong>; Display a <strong>confusion matrix</strong> showing classification prediction hits and misses; Perform <strong>multiple linear regression</strong> with the <strong>California Housing dataset</strong>; Perform <strong>dimensionality reduction</strong> with <strong>PCA</strong> and <strong>t-SNE</strong> on the <strong>Iris</strong> and <strong>Digits datasets</strong> to prepare them for <strong>two-dimensional visualizations</strong>. Perform <strong>unsupervised machine learning</strong> with <strong>k-means clustering</strong> and the Iris dataset.<br/>\n<br/>\n</li><li><strong>Lesson 15—Deep Learning</strong>—What a <strong>neural network</strong> is and how it enables <strong>deep learning</strong>; Create <strong>Keras neural networks</strong>;<strong>Keras</strong> <strong>layers</strong>, <strong>activation functions</strong>, <strong>loss functions</strong> and <strong>optimizers</strong>; Use a Keras <strong>convolutional neural network (CNN)</strong> trained on the <strong>MNIST dataset</strong> to build a computer vision application that <strong>recognizes handwritten digits</strong>; Use a Keras <strong>recurrent neural network (RNN)</strong> trained on the <strong>IMDb dataset</strong> to create a sentiment analysis application that performs <strong>binary classification</strong> of <strong>positive and negative movie reviews</strong>.<br/>\n<br/>\n</li><li><strong>Lesson 16—Big Data: Hadoop, Spark, 17</strong>—Manipulate a <strong>SQLite relational database using SQL</strong>; Understand the four major <strong>types of NoSQL databases</strong>; Store tweets in a <strong>MongoDB NoSQL JSON document database</strong> and visualize them on a <strong>Folium map</strong>; <strong>Apache Hadoop</strong> and how it’s used in big-data batch-processing applications; Build a <strong>Hadoop MapReduce</strong> application on <strong>Microsoft’s Azure HDInsight cloud service</strong>; <strong>Apache Spark</strong> and how it’s used in high-performance, real-time big-data applications; Process mini-batches of data with <strong>Spark streaming</strong>; <strong>Internet of Things (IoT)</strong> and the <strong>publish/subscribe model</strong>; Publish messages from a simulated Internet-connected device and <strong>visualize messages in a dashboard</strong>; Subscribe to PubNub’s sample live streams and visualize the data.</li></ul><p>LiveLessons Video Training series publishes hundreds of hands-on, expert-led video tutorials covering a wide selection of technology topics designed to teach you the skills you need to succeed. This professional and personal technology video series features world-leading author instructors published by your trusted technology brands: Addison-Wesley, Cisco Press, IBM Press, Pearson IT Certification, Prentice Hall, Sams, and Que. Topics include: IT Certification, Programming, Web Development, Mobile Development, Home &amp; Office Technologies, Business &amp; Management, and more. View All LiveLessons on InformIT: <a href=\"http://www.informit.com/imprint/series_detail.aspx?ser=2185116\">http://www.informit.com/imprint/series_detail.aspx?ser=2185116</a></p></span>",
            "average_rating": 4935,
            "number_of_followers": 0,
            "number_of_items": 0,
            "number_of_reviews": 31,
            "popularity": 999967990,
            "report_score": 153000,
            "cover_url": "https://learning.oreilly.com/library/cover/9780135917411/",
            "date_added": "2019-04-03T21:55:14.126Z",
            "topics": [
                "cda50ea0-3a3a-4d54-89bb-a7a4179365e6"
            ],
            "topics_payload": [
                {
                    "uuid": "cda50ea0-3a3a-4d54-89bb-a7a4179365e6",
                    "slug": "python",
                    "name": "Python",
                    "score": null
                }
            ],
            "save_link": "http://localhost:8000/api/v1/save_book/?book_id_o=9780135917411"
        }
}
    `
 
