json.extract! mluserinput, :id, :title, :subject, :subtopics, :mlinput, :created_at, :updated_at
json.url mluserinput_url(mluserinput, format: :json)
