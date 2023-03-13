require "application_system_test_case"

class MluserinputsTest < ApplicationSystemTestCase
  setup do
    @mluserinput = mluserinputs(:one)
  end

  test "visiting the index" do
    visit mluserinputs_url
    assert_selector "h1", text: "Mluserinputs"
  end

  test "should create mluserinput" do
    visit mluserinputs_url
    click_on "New mluserinput"

    fill_in "Mlinput", with: @mluserinput.mlinput
    fill_in "Subject", with: @mluserinput.subject
    fill_in "Subtopics", with: @mluserinput.subtopics
    fill_in "Title", with: @mluserinput.title
    click_on "Create Mluserinput"

    assert_text "Mluserinput was successfully created"
    click_on "Back"
  end

  test "should update Mluserinput" do
    visit mluserinput_url(@mluserinput)
    click_on "Edit this mluserinput", match: :first

    fill_in "Mlinput", with: @mluserinput.mlinput
    fill_in "Subject", with: @mluserinput.subject
    fill_in "Subtopics", with: @mluserinput.subtopics
    fill_in "Title", with: @mluserinput.title
    click_on "Update Mluserinput"

    assert_text "Mluserinput was successfully updated"
    click_on "Back"
  end

  test "should destroy Mluserinput" do
    visit mluserinput_url(@mluserinput)
    click_on "Destroy this mluserinput", match: :first

    assert_text "Mluserinput was successfully destroyed"
  end
end
