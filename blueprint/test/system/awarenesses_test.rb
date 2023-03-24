require "application_system_test_case"

class AwarenessesTest < ApplicationSystemTestCase
  setup do
    @awareness = awarenesses(:one)
  end

  test "visiting the index" do
    visit awarenesses_url
    assert_selector "h1", text: "Awarenesses"
  end

  test "should create awareness" do
    visit awarenesses_url
    click_on "New awareness"

    fill_in "Subject", with: @awareness.subject
    fill_in "Subtopics", with: @awareness.subtopics
    fill_in "Title", with: @awareness.title
    click_on "Create Awareness"

    assert_text "Awareness was successfully created"
    click_on "Back"
  end

  test "should update Awareness" do
    visit awareness_url(@awareness)
    click_on "Edit this awareness", match: :first

    fill_in "Subject", with: @awareness.subject
    fill_in "Subtopics", with: @awareness.subtopics
    fill_in "Title", with: @awareness.title
    click_on "Update Awareness"

    assert_text "Awareness was successfully updated"
    click_on "Back"
  end

  test "should destroy Awareness" do
    visit awareness_url(@awareness)
    click_on "Destroy this awareness", match: :first

    assert_text "Awareness was successfully destroyed"
  end
end
