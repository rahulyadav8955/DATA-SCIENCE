library(shiny)
ui <- fluidPage(
 titlePanel("Prediction"),
   sidebarLayout(
    sidebarPanel(
      numericInput("num","Numeric input",1)
    ),
    mainPanel(
      tableOutput("distplot")
      
    )
  )
)
server <- function(input, output) {
  output$distplot <- renderTable({
    
    wc_at <- read.csv("D:/Data Science/Data Science/RCodes/Simple Linear Regression/wc-at.csv")
    
    reg_log <- lm(AT ~ log(Waist),data = wc_at)
    nw=data.frame(Waist=input$num)
    nw
    w=predict(reg_log,nw)
    w
  })
  
}

shinyApp(ui = ui, server = server)
