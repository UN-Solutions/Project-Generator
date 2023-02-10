json.extract! userinput, :id, :title, :subject, :subtopics, :created_at, :updated_at
json.url userinput_url(userinput, format: :json)
