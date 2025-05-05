        def sidebar_image(self,name):
            self.side_bar_img = Image.open(f"images/{name}")
            self.side_bar_img = self.side_bar_img.resize((30, 30))
            self.side_bar_image = ImageTk.PhotoImage(self.side_bar_img)
            return self.side_bar_image

        condition_sidebar = ["True"]
        text_data = []
        def collapse_sidebar(self,condition,data):
            #messagebox.showinfo("Info",condition_sidebar[0])
            if condition == "True":
                self.side_bar_image = sidebar_image(self,"side_right.png")
                self.side_bar_button.config(image=self.side_bar_image)
                for i in data:
                    text_data.append(i["text"])
                    self.frame_left.config(width=100)
                    i.config(width=100,text='',fg='steelblue')
                condition_sidebar[0] = "False"
            else:
                self.frame_left.config(width=250)
                self.side_bar_image = sidebar_image(self, "side_left.png")
                self.side_bar_button.config(image=self.side_bar_image)
                for j in data:
                    j.config(width=250,text=text_data[0],fg='white')
                    del text_data[0]
                condition_sidebar[0] = "True"
            #messagebox.showinfo("Info",data)

        data = [self.user_account_button,self.home_page_button,self.peoples_page_button,self.friends_page_button,self.post_page_button]

        self.side_bar_image = sidebar_image(self,"side_left.png")
        self.side_bar_button = Button(self.frame_left,image = self.side_bar_image,border=0,cursor="hand2",command = lambda: collapse_sidebar(self,condition_sidebar[0],data))
        self.side_bar_button.place(x=0,y=5)
