require "application_system_test_case"

class PresentationsTest < ApplicationSystemTestCase
  setup do
    @presentation = presentations(:one)
  end

  test "visiting the index" do
    visit presentations_url
    assert_selector "h1", text: "Presentations"
  end

  test "should create presentation" do
    visit presentations_url
    click_on "New presentation"

    fill_in "Subject", with: @presentation.subject
    fill_in "Subtopics", with: @presentation.subtopics
    fill_in "Title", with: @presentation.title
    click_on "Create Presentation"

    assert_text "Presentation was successfully created"
    click_on "Back"
  end

  test "should update Presentation" do
    visit presentation_url(@presentation)
    click_on "Edit this presentation", match: :first

    fill_in "Subject", with: @presentation.subject
    fill_in "Subtopics", with: @presentation.subtopics
    fill_in "Title", with: @presentation.title
    click_on "Update Presentation"

    assert_text "Presentation was successfully updated"
    click_on "Back"
  end

  test "should destroy Presentation" do
    visit presentation_url(@presentation)
    click_on "Destroy this presentation", match: :first

    assert_text "Presentation was successfully destroyed"
  end
end
