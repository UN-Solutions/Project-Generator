require "application_system_test_case"

class UserinputsTest < ApplicationSystemTestCase
  setup do
    @userinput = userinputs(:one)
  end

  test "visiting the index" do
    visit userinputs_url
    assert_selector "h1", text: "Userinputs"
  end

  test "should create userinput" do
    visit userinputs_url
    click_on "New Future Planning"

    fill_in "Subject", with: @userinput.subject
    fill_in "Subtopics", with: @userinput.subtopics
    fill_in "Title", with: @userinput.title
    click_on "Create Future Planning"

    assert_text "Future Planning item was successfully created"
    click_on "Back"
  end

  test "should update Userinput" do
    visit userinput_url(@userinput)
    click_on "Edit this item", match: :first

    fill_in "Subject", with: @userinput.subject
    fill_in "Subtopics", with: @userinput.subtopics
    fill_in "Title", with: @userinput.title
    click_on "Update item"

    assert_text "Future Planning item was successfully updated"
    click_on "Back"
  end

  test "should destroy Userinput" do
    visit userinput_url(@userinput)
    click_on "Destroy this item", match: :first

    assert_text "Future Planning item was successfully destroyed"
  end
end
