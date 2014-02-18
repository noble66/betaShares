def html_template(email, was_submitted=False):
    return '''<html>
    
    <head>
    
 <style media="screen" type="text/css">
        body { background-color:rgb(245,245,245); }
       .layer1_class { text-align:center; width:100%; position: absolute; z-index: 1; top: 150px; left: 0px; visibility: visible; }
      .layer2_class {
            position: relative;
            z-index: 2;
            width:760px;
            top: 10px;
            visibility: hidden;
            margin-left:auto;
            margin-right:auto;
            padding: 15px 40px;
            padding-bottom:5px;
            margin-bottom:50px;
            background-color:white;
        }
        .header {
            text-align:center;
            font-size:32px;
            font-family:Georgia, serif;
            padding:20px;
        }
        .comment {
            text-align:center;
            font-size:16px;
            font-family:Helvetica, sans-serif;
            padding-bottom:20px;
            color:rgb(128,128,128);
        }
        .submitted {
            text-align:center;
            font-family:'Helvetica',sans-serif;
            font-size:14px;
            padding-bottom:15px;
            color:rgb(103,155,59);
            display:none;
        }
        .recommend {
            font-style:italic;
            color:#999;
        }
        .layer2_class hr {
            border:0px;
            border-top:1px solid rgb(205,205,205);
            border-style:solid;
            margin-bottom:0;
            margin-top:15px;
        }
        .layer2_class li {
            list-style-type:none;
        }

        .layer2_class h3 {
            margin-bottom:0px;
        }

        .layer2_class a {
            color:rgb(34,34,34);
            text-decoration:none;
        }
        .layer2_class a:hover {
            text-decoration:underline;
        }
        .layer2_class .rd-pub {
            margin-bottom:10px;
        }
        .layer2_class .st {
            display:block;
            min-height:50px;
        }
        input[type="submit"] {
            display:block;
            margin-left:auto;
            margin-right:auto;
            background:none;
            background-color:white;
            color:#333;
            border: 1px #333 solid;
            border-radius:.5em;
            font-size:16px;
            padding:10px 15px;
        }
        input[type="submit"] {
        display:block;
        margin-left:auto;
        margin-right:auto;
        background:none;
        background-color:white;
        color:#333;
        border: 1px #333 solid;
        border-radius:.5em;
        font-size:16px;
        padding:10px 15px;
        cursor:pointer;
    }
    </style>
    <script>
      function downLoad(){
        var xhr = new XMLHttpRequest();
        xhr.open("GET", "/<SUMAN FILL THIS EP>/" + email)
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4) {
                if (xhr.status == 200) {
                    if (document.all){
                        document.all["layer1"].style.visibility="hidden";
                        document.all["layer2"].style.visibility="visible";
                        document.all["layer2"].innerHTML = xhr.responseText;
                    } else if (document.getElementById){
                        document.getElementById("layer1").style.visibility='hidden';
                        document.getElementById("layer2").style.visibility='visible';
                        document.getElementById("layer2").innerHTML = xhr.responseText;
                    }
                }
            }
        }
        
        was_submitted = document.getElementById('has_submitted').value;
        if (was_submitted == 'True') {
            submitted = document.getElementsByClassName('submitted')[0];
            submitted.style.display = 'block';
        }
      }
    </script>

    
    </head>

   <body onload="downLoad()">
    <input type="hidden" id="has_submitted" value="''' + str(was_submitted) + '''"/>

    
    <div class="header">Instapaper <span class="recommend">Recommended</span></div>
    
    <div class="comment"><span class="comment">  Thanks for testing our new recommendations feature. <br> Rate the relevance of the stories below to help us optimize your recommendations. </span></div>
    
    <div class="submitted">Thanks for submitting your feedback! Here are your updated recommendations:</div>
    
   <div id="layer1" class="layer1_class">
          <strong>Please wait while we re-rank results ..</strong>
    </div>
    
    <div id="layer2" class="layer2_class">
    </div>
    </body>
    </html>
    '''

# prepares the html to show to feedback users. 
def vertical_tbl(vData, previousFeedback, email='', was_submitted=False):
    vLinks = vData['entries'].keys()
    linksPrevious = ut.fpd_dl(previousFeedback)
    dataRes = ''

    for link in vLinks:
        checkVal = ''
        if link in linksPrevious:
            checkVal=linksPrevious[link]
        if 'title' in vData['entries'][link] and 'description' in vData['entries'][link]:
            if 'image' in vData['entries'][link]:
                imag = vData['entries'][link]['image']
            else:
                imag = "http://isource.com/wp-content/uploads/2013/12/instapaper-logo1.jpg"
            dataRes+='''<li class="g _n">'''
            dataRes+=''' <div class="rc" data-hveid="139"><!--m-->
                        <div style="float:left;margin-right:15">
                        <div class="th _Dk" style="height:250px;width:250px">
                            <a href="http://'''+ link+'''" target="_blank">
                            <img height="160" id='''+link+''' src="'''+imag+'''"  width="220" border="0" ></a>
                        </div>
                    </div>
                    <div style="margin-left:0px;padding-bottom:0">
                        <h3 class="r">
                        <a href="http://'''+link+'''" target="_blank" ><b>'''+vData['entries'][link]['title']+'''</b></a></h3>
                    <div class="s" style="max-width:749px"><div class="rd-pub rd-pub-desktop"><cite>'''+iu.get_Domain(link)+'''</cite> -
                    <div class="rd-pub-date"></div></div><span class="st rd-snippet">'''+vData['entries'][link]['description'][:250]+''' ...</span>
                    <div class="rd-label">
      '''
            if  checkVal=='':
                formHtml = ''' <br>
                            <form action ="/instaFeedback_post" method="POST">
                                <fieldset>
                                 <legend> Feedback </legend>
                                 <p>
                                    <label></label>            
                                    <input type = "radio"
                                           name = "'''+str(link)+'''"
                                           id = "relevant"
                                           value = "Relevant"
                                            />
                                    <label for = "relevant">Relevant</label>
                                    
                                    <input type = "radio"
                                           name = "'''+str(link)+'''"
                                           id = "ok"
                                           value = "Curious" />
                                    <label for = "ok">Somewhat Relevant</label> '''
            elif checkVal=='curious':
                formHtml = ''' <br>
                            <form action ="/instaFeedback_post" method="POST">
                                <fieldset>
                                 <legend> Feedback </legend>
                                 <p>
                                    <label></label>            
                                    <input type = "radio"
                                           name = "'''+str(link)+'''"
                                           id = "relevant"
                                           value = "Relevant"
                                            />
                                    <label for = "relevant">Relevant</label>
                                    
                                    <input type = "radio"
                                           name = "'''+str(link)+'''"
                                           id = "ok"
                                           value = "Curious" checked />
                                    <label for = "ok"><em>Somewhat Relevant </em></label> '''
            elif checkVal=='relevant':
                formHtml = ''' <br>
                            <form action ="/instaFeedback_post" method="POST">
                                <fieldset>
                                 <legend> Feedback </legend>
                                 <p>
                                    <label></label>            
                                    <input type = "radio"
                                           name = "'''+str(link)+'''"
                                           id = "relevant"
                                           value = "Relevant"
                                            checked />
                                    <label for = "relevant"><em>Relevant</em></label>
                                    
                                    <input type = "radio"
                                           name = "'''+str(link)+'''"
                                           id = "ok"
                                           value = "Curious"  />
                                    <label for = "ok">Somewhat Relevant</label> '''
                           
            formHtml+='''<input type = "radio"
                                           name = "'''+str(link)+'''"
                                           id = "notrel"
                                           value = "Not Relevant" />
                                    <label for = "notrel">Not Relevant</label>
                                    
                                    <input type = "radio"
                                           name = "'''+str(link)+'''"
                                           id = "notrel"
                                           value = "Already Seen" />
                                    <label for = "notrel">Already Seen</label>
                                  </p>       
                                </fieldset>
                              
                        '''
            dataRes +=formHtml
            dataRes += '''<br><hr><br>'''
      
    optional = '''Explore:
      <a style="text-decoration:none" href="/search?safe=active&amp;q=twitter+instagram&amp;tbs=ida:1&amp;sa=X&amp;ei=uu_vUu_GGuqssQTEqYDwCA&amp;ved=0CI8BEK8xMAw">twitter instagram</a></div></div></div><div style="clear:left"></div><!--n--></div></li>
      '''
    
    formControl = '''
    <input type = "hidden"
                name = "username"
                id = "username"
                value = "'''+str(ut.all_slash_die(email))+'''" /> 
    
    
    <textarea style="font-size:16px;width:100%;height:100px;resize:none;margin-bottom:30px;padding:5px;" name="userFeedback" placeholder="Other feedback..."></textarea>
    
    <br>
    <input type="submit" value="Submit!" />
                            </form>
    '''
    
    dataRes+=formControl
    return dataRes
