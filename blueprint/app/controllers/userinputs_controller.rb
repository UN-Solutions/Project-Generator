class UserinputsController < ApplicationController
  before_action :set_userinput, only: %i[ show edit update destroy ]
  # GET /userinputs or /userinputs.json
  def download_pdf
    send_file "#{Rails.root}/future.pdf", type: "application/pdf", x_sendfile: true
  end

  def index
    @userinputs = Userinput.all
    @our_input = Userinput.order("id DESC").first
    @output = `python3 future.py "#{@our_input.inspect}"`

  end

  # GET /userinputs/1 or /userinputs/1.json
  def show
  end

  # GET /userinputs/new
  def new
    @userinput = Userinput.new
  end

  # GET /userinputs/1/edit
  def edit
  end

  # POST /userinputs or /userinputs.json
  def create
    @userinput = Userinput.new(userinput_params)

    respond_to do |format|
      if @userinput.save
        format.html { redirect_to userinput_url(@userinput), notice: "Userinput was successfully created." }
        format.json { render :show, status: :created, location: @userinput }
      else
        format.html { render :new, status: :unprocessable_entity }
        format.json { render json: @userinput.errors, status: :unprocessable_entity }
      end
    end
  end

  # PATCH/PUT /userinputs/1 or /userinputs/1.json
  def update
    respond_to do |format|
      if @userinput.update(userinput_params)
        format.html { redirect_to userinput_url(@userinput), notice: "Userinput was successfully updated." }
        format.json { render :show, status: :ok, location: @userinput }
      else
        format.html { render :edit, status: :unprocessable_entity }
        format.json { render json: @userinput.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /userinputs/1 or /userinputs/1.json
  def destroy
    @userinput.destroy

    respond_to do |format|
      format.html { redirect_to userinputs_url, notice: "Userinput was successfully destroyed." }
      format.json { head :no_content }
    end
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_userinput
      @userinput = Userinput.find(params[:id])
    end

    # Only allow a list of trusted parameters through.
    def userinput_params
      params.require(:userinput).permit(:title, :subject, :subtopics)

    end
end
