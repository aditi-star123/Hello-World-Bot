from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
from telegram.ext import MessageHandler
from telegram.ext import filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

# Define your bot token


# Define command handler functions as asynchronous
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        await update.message.reply_text("Hello! Welcome to the ChatBot")
    except Exception as e:
        await update.message.reply_text("Something went wrong. Please try again later.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        '''
        /start - Welcome to the channel..hope you are doing well😊!!
        /help -🧒 this particular message
        /content - 🧑‍🏫This bot is designed to assist you in finding the best resources for your placements and core topics.
        /blogs_and_articles - A list of articles
        /recommend -👉First type this command followed by your message and if we have them we will provide you the link.
        /web_development- 🤗Web development project ideas and tutorials.
        /competitive_programming - 👩‍🏫Competitive programming is to keep you ahead of other students.
        /feedback - Thank you for using our bot! We greatly value your input and would love to hear your thoughts on how we can enhance your experience.
        '''
    )

# Blogs and articles related
async def blogs_and_articles(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Web Dev Blogs", callback_data='web dev blogs')],
        [InlineKeyboardButton("Tech Opportunities", callback_data='tech_opportunities')],
        [InlineKeyboardButton("Boost LinkedIn", callback_data='boost_linkedin')],
        [InlineKeyboardButton("Resume Prep Tips", callback_data='resume_prep')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Choose a topic to explore:', reply_markup=reply_markup)

# Defining the Button Handler
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query  # Corrected this line
    query.answer()
    data = query.data 
    responses = {
        'web dev blogs': "Check out these web development blogs:\n1. [Blog 1](https://blog.miguelgrinberg.com/index)",
        'resume_prep': "Here are some tips for resume preparation:\n1. [Tip 1](https://edu.gcfglobal.org/en/resumewriting/resume-tips-and-strategies/1/)\n2. [Tip 2](https://www.linkedin.com/pulse/resume-writing-tips-make-your-stand-out-mnr-solutions-pvt-ltd/)",
        'boost_linkedin': "Learn how to boost your LinkedIn profile:\n1. [Guide 1](https://www.linkedin.com/pulse/how-stand-out-linkedin-5-tips-boost-your-profile-talentfoot/)\n2. [Guide 2](https://www.linkedin.com/business/sales/blog/profile-best-practices/17-steps-to-a-better-linkedin-profile-in-2017)",
        'tech_opportunities': "Explore tech opportunities:\n1. [Opportunity 1](https://medium.com/@praveenankita1967/all-the-tech-opportunities-you-need-to-know-about-wwcd-week-3-3d944c509eb9)",
    } 
    response = responses.get(data, "Sorry, I don't have information for that option.")
    await query.edit_message_text(text=response)

async def content(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("We have various playlists available")

# Allow users to specify their interests (e.g., Python, SQL, Java).
# Suggest resources based on their preferences.
async def recommend(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_interest = ' '.join(context.args).lower()
    recommendations = {  # recommendations is a dictionary
        'python': "Check out this Python tutorial: https://www.youtube.com/watch?v=7wnove7K-ZQ",
        'sql': "Explore SQL with this guide: https://www.youtube.com/watch?v=323H_mOOWQ4",
        'java': "Start learning Java here: https://www.youtube.com/watch?v=UmnCZ7-9yDY"
    }
    response = recommendations.get(user_interest, "Sorry, I don't have resources for that topic.")
    await update.message.reply_text(response)


#web development and flutter resources

#first we need to define the resources(dictionary)

resources={
   
"cheatsheets": [
        "HTML/CSS Cheat Sheet: [Link](https://html.com/blog/100-web-development-cheat-sheets/)",
        
    ],
    "roadmaps": [
        "Frontend Development Roadmap: [Link](https://www.youtube.com/watch?v=DbRXv5TXMEE)",
        "Backend Development Roadmap: [Link](https://www.youtube.com/watch?v=AL6U8-pggcU)",
    ],
    "practice_channels": [
        "FreeCodeCamp: [Link](https://www.freecodecamp.org/learn/)",
        "Codewars: [Link](https://www.codewars.com/)",
    ],
    "projects": [
        "FOR BEGINNERS IN WEB DEVLOPMENT"
        
        "Personal Portfolio: Build a portfolio website to showcase your work.",
        "E-commerce Site: Create a simple e-commerce website with basic functionalities.",
        "Personal Portfolio website"

        "INTERMEDIATE PROJECTS"
        "Recipe finder: A web app that allows users to search for recipes based on ingredients they have."
        "Task management app: Build a more advanced task manager with user authentication, project categories, and deadline reminders"

        "SOME ADVANCE LEVEL PROJECTS"
        "Real time application: Develop a chat application with real-time messaging, private chats, and chat rooms."
        "Custom Content Management System (CMS): Develop a CMS where users can manage and create dynamic content for their websites, including templates and user roles"
    ]
}
async def webdev(update:Update,context:ContextTypes.DEFAULT_TYPE)->None:
    msg="Here are some useful Web development resources:\n"

    for category,items in resources.items():
        msg+=f"*{category.capitalize()}*\n"
        for item in items:
            msg += f"• {item}\n"
        msg += "\n"
    
    await update.message.reply_text(msg, parse_mode='Markdown')



    

async def cp(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("In light of the current economic downturn and increased competition in the job market, it's crucial to stay ahead of the curve. To support you in this endeavor, I have curated a collection of top-notch competitive programming resources. Do check out this link: https://github.com/kunal-kushwaha/Competitive-Programming-Resources")

async def scholarships(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Scholarships play a crucial role in making education accessible and affordable. They provide financial assistance to cover tuition fees, books, and other expenses, allowing students to focus on their studies without the burden of debt. Scholarships also recognize and reward academic excellence, support underrepresented groups, and can open doors to further opportunities for personal and professional growth. In today's competitive job market, having access to such resources can significantly impact your educational journey and career prospects. Explore a variety of scholarships available to support your educational journey. Check out these opportunities to find one that suits your needs: [Scholarships 1](https://code.likeagirl.io/15-scholarships-for-women-in-tech-61f0cb242be1)")

async def feedback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    feedback_message = ' '.join(context.args)
    await update.message.reply_text("Thank you for the feedback")

#for handling if user enters any unwanted text
async def unknown(update:Update,context:ContextTypes.DEFAULT_TYPE) -> None: 
    message="Sorry I don't understand that ☹️. Please use /start to get started or send me something else!"
    await update.message.reply_text(message)

# Create the application and pass it your bot's token
application = ApplicationBuilder().token(TOKEN).build()
application.add_handler(CommandHandler("blogs_and_articles", blogs_and_articles))
application.add_handler(CallbackQueryHandler(button))

# Add handlers for commands
application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("help", help_command))
application.add_handler(CommandHandler("content", content))
application.add_handler(CommandHandler("recommend", recommend))
application.add_handler(CommandHandler("web_development",webdev))
application.add_handler(CommandHandler("competitive_programming", cp))
application.add_handler(CommandHandler("scholarships", scholarships))
application.add_handler(CommandHandler("feedback", feedback))

#add message handler for unknown text
application.add_handler(MessageHandler(filters.text & ~filters.COMMAND,unknown))


# Start the bot
if __name__ == "__main__":
    application.run_polling()
