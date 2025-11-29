from manim import *
import numpy as np

class AI_Memory_Solution_Video(Scene):
    def construct(self):
        self.camera.background_color = "#0f172a"
        
        self.demonstrate_memory_problem()     
        self.introduce_cilow_solution()       
        self.show_multi_platform_demo()       
        self.create_final_call_to_action()     

    def demonstrate_memory_problem(self):
        title = Text("The Problem: AI Has No Memory", font_size=36, color="#ef4444", weight=BOLD)
        title.to_edge(UP, buff=0.8)
        self.play(Write(title), run_time=1)
        
        user = self.create_user_avatar()
        user.move_to(LEFT * 6.5)
        
        chatgpt_window = self.create_chat_window("ChatGPT", "#74aa9c")
        chatgpt_window.move_to(LEFT * 2.0 + UP * 0.5)
        
        claude_window = self.create_chat_window("Claude", "#ff6b35") 
        claude_window.move_to(RIGHT * 2.0 + UP * 0.5)
        
        self.play(
            FadeIn(user),
            FadeIn(chatgpt_window),
            FadeIn(claude_window),
            run_time=1.2
        )
        
        user_message = "I prefer aisle seats while flying. But for long flights make it a window seat."
        
        first_message = self.create_chat_bubble(user_message, True)
        first_message.move_to(user.get_center() + RIGHT * 1.5)
        self.play(FadeIn(first_message), run_time=0.6)
        
        self.play(
            first_message.animate.move_to(chatgpt_window[4].get_center() + UP * 0.5),
            run_time=1.2
        )
        
        chatgpt_user_msg = self.create_chat_bubble(user_message, True)
        chatgpt_user_msg.move_to(chatgpt_window[4].get_center() + UP * 0.5)
        
        chatgpt_response = self.create_chat_bubble("Noted your seat preference. I'll remember this for future travel planning.", False)
        chatgpt_response.move_to(chatgpt_window[4].get_center() + DOWN * 0.3)
        
        self.remove(first_message)
        self.add(chatgpt_user_msg)
        
        self.wait(0.3)
        self.play(FadeIn(chatgpt_response), run_time=0.6)
        
        second_message = self.create_chat_bubble(user_message, True)
        second_message.move_to(user.get_center() + RIGHT * 1.5)
        self.play(FadeIn(second_message), run_time=0.6)
        
        self.play(
            second_message.animate.move_to(claude_window[4].get_center() + UP * 0.5),
            run_time=1.2
        )
        
        claude_user_msg = self.create_chat_bubble(user_message, True)
        claude_user_msg.move_to(claude_window[4].get_center() + UP * 0.5)
        
        self.remove(second_message)
        self.add(claude_user_msg)
        
        claude_response = self.create_chat_bubble("I don't know your seat preferences. Could you tell me?", False)
        claude_response.move_to(claude_window[4].get_center() + DOWN * 0.3)
        
        self.wait(0.3)
        self.play(FadeIn(claude_response), run_time=0.6)
        
        problem_indicators = VGroup()

        memory_lost_indicator = VGroup()
        memory_icon = Text("💨", font_size=20)
        memory_text = Text("Memory Lost", font_size=16, color="#ef4444", weight=BOLD)
        memory_text.next_to(memory_icon, RIGHT, buff=0.2)
        memory_lost_indicator.add(memory_icon, memory_text)
        memory_lost_indicator.move_to([5.0, 0.5, 0])

        repeat_indicator = VGroup()
        repeat_icon = Text("🔁", font_size=20)
        repeat_text = Text("Forced to Repeat", font_size=16, color="#ef4444", weight=BOLD)
        repeat_text.next_to(repeat_icon, RIGHT, buff=0.2)
        repeat_indicator.add(repeat_icon, repeat_text)
        repeat_indicator.move_to([5.0, -0.2, 0])

        problem_indicators.add(memory_lost_indicator, repeat_indicator)

        self.play(LaggedStartMap(FadeIn, problem_indicators, lag_ratio=0.2), run_time=1.0)
        
        stat_cards = VGroup()
        stat_numbers = [
            ("40%", "of time wasted\nrepeating information"),
            ("$52K", "annual productivity\ncost per team"), 
            ("70%", "of conversations are\nrepetitive across AIs"),
        ]

        for i, (number, description) in enumerate(stat_numbers):
            stat_card = self.create_stat_card(number, description)
            x_position = -4.5 + i * 4.5
            y_position = -3.1
            stat_card.move_to([x_position, y_position, 0])
            stat_cards.add(stat_card)

        self.play(LaggedStartMap(FadeIn, stat_cards, lag_ratio=0.2), run_time=1.5)
        
        self.wait(2)
        
        self.play(
            FadeOut(title),
            FadeOut(user),
            FadeOut(chatgpt_window),
            FadeOut(claude_window),
            FadeOut(chatgpt_user_msg),
            FadeOut(chatgpt_response),
            FadeOut(claude_user_msg),
            FadeOut(claude_response),
            FadeOut(problem_indicators),
            FadeOut(stat_cards),
            run_time=1.2
        )

    def create_stat_card(self, number, description):
        card_background = RoundedRectangle(
            height=1.4, width=2.5,
            fill_color="#1e293b", fill_opacity=1,
            stroke_color="#ef4444", stroke_width=2,
            corner_radius=0.2
        )
        
        number_display = Text(number, font_size=20, color="#ef4444", weight=BOLD)
        number_display.move_to(card_background.get_center() + UP * 0.3)
        
        description_text = Text(description, font_size=10, color=GRAY_B, line_spacing=1.2)
        description_text.set_width(card_background.width * 0.8)
        description_text.move_to(card_background.get_center() + DOWN * 0.2)
        
        return VGroup(card_background, number_display, description_text)

    def create_user_avatar(self):
        avatar_circle = Circle(radius=0.6, fill_color="#1e293b", fill_opacity=1,
                          stroke_color="#eab308", stroke_width=3)
        
        user_icon = Text("👤", font_size=24)
        user_icon.move_to(avatar_circle.get_center())
        
        user_name = Text("Chetan", font_size=12, color="#eab308", weight=BOLD)
        user_name.next_to(avatar_circle, DOWN, buff=0.15)
        
        return VGroup(avatar_circle, user_icon, user_name)

    def create_chat_window(self, platform_name, accent_color):
        window_frame = RoundedRectangle(
            height=3.2, width=3.0,
            fill_color="#1e293b", fill_opacity=1,
            stroke_color=accent_color, stroke_width=2,
            corner_radius=0.3
        )
        
        header_bar = Rectangle(
            height=0.6, width=3.0,
            fill_color=accent_color, fill_opacity=0.9,
            stroke_color=accent_color
        )
        header_bar.move_to(window_frame.get_top() + DOWN * 0.3)
        
        app_icon = Circle(radius=0.15, fill_color=WHITE, fill_opacity=0.9, stroke_width=0)
        app_icon.move_to(header_bar.get_left() + RIGHT * 0.35)
        
        name_label = Text(platform_name, font_size=12, color=WHITE, weight=BOLD)
        name_label.move_to(header_bar.get_center())
        
        message_area = Rectangle(
            height=2.0, width=2.7,
            fill_color="#0f172a", fill_opacity=1,
            stroke_color="#334155", stroke_width=1
        )
        message_area.move_to(window_frame.get_center() + UP * 0.1)
        
        input_field = RoundedRectangle(
            height=0.4, width=2.5,
            fill_color="#1e293b", fill_opacity=1,
            stroke_color="#475569", stroke_width=1,
            corner_radius=0.2
        )
        input_field.move_to(window_frame.get_bottom() + UP * 0.3)
        
        return VGroup(window_frame, header_bar, app_icon, name_label, message_area, input_field)

    def create_chat_bubble(self, message_text, is_user_message):
        if is_user_message:
            bubble_color = "#3b82f6"
            text_color = WHITE
        else:
            bubble_color = "#374151"
            text_color = WHITE
        
        text_content = Text(message_text, font_size=9, color=text_color, line_spacing=1.1)
        text_content.set_width(2.2)
        
        min_bubble_height = 0.6
        calculated_height = max(text_content.height + 0.15, min_bubble_height)
        
        message_bubble = RoundedRectangle(
            height=calculated_height,
            width=text_content.width + 0.2,
            fill_color=bubble_color, fill_opacity=1,
            stroke_color=bubble_color,
            corner_radius=0.1
        )
        
        text_content.move_to(message_bubble.get_center())
        return VGroup(message_bubble, text_content)

    def introduce_cilow_solution(self):
        main_title = Text("Cilow: AI's Persistent Memory", font_size=32, color="#3b82f6", weight=BOLD)
        main_title.to_edge(UP, buff=1.0)
        
        sub_title = Text("One memory system for all AI Agents", font_size=18, color=GRAY_B)
        sub_title.next_to(main_title, DOWN, buff=0.1)
        
        self.play(Write(main_title), FadeIn(sub_title), run_time=1)
        
        cilow_hub = self.create_memory_hub()
        cilow_hub.move_to([0, 0.8, 0])
        self.play(DrawBorderThenFill(cilow_hub), run_time=1.2)
        
        ai_platforms = VGroup()
        platform_configs = [
            {"name": "ChatGPT", "icon": "🤖", "color": "#74aa9c", "position": [-4.8, -0.5, 0]},
            {"name": "Claude", "icon": "📚", "color": "#ff6b35", "position": [4.8, -0.5, 0]},
            {"name": "Gemini", "icon": "💎", "color": "#8a2be2", "position": [-4.8, -2.5, 0]},
            {"name": "Perplexity", "icon": "🔍", "color": "#00a8e8", "position": [4.8, -2.5, 0]},
        ]
        
        for config in platform_configs:
            platform = self.create_platform_badge(config["name"], config["icon"], config["color"])
            platform.move_to(config["position"])
            ai_platforms.add(platform)
        
        self.play(LaggedStartMap(FadeIn, ai_platforms, lag_ratio=0.15), run_time=1.5)
        
        connection_lines = VGroup()
        for platform in ai_platforms:
            line = DashedLine(
                platform[0].get_center(), 
                cilow_hub[0].get_center(),
                color=GREEN, 
                stroke_width=2, 
                stroke_opacity=0.6
            )
            connection_lines.add(line)
        
        self.play(LaggedStartMap(Create, connection_lines, lag_ratio=0.1), run_time=1.2)
        
        save_animations = VGroup()
        for platform in ai_platforms:
            dot = Dot(radius=0.08, color=GREEN, fill_opacity=1)
            dot.move_to(platform[0].get_center())
            save_animations.add(dot)
        
        self.play(
            *[dot.animate.move_to(cilow_hub[0].get_center()) for dot in save_animations],
            run_time=1.5
        )
        self.play(FadeOut(save_animations))
        
        retrieve_animations = VGroup()
        for platform in ai_platforms:
            dot = Dot(radius=0.08, color=BLUE, fill_opacity=1)
            dot.move_to(cilow_hub[0].get_center())
            retrieve_animations.add(dot)
        
        self.play(
            *[dot.animate.move_to(ai_platforms[i][0].get_center()) for i, dot in enumerate(retrieve_animations)],
            run_time=1.5
        )
        self.play(FadeOut(retrieve_animations))
        
        feature_highlights = VGroup()
        feature_list = [
            ("💾 Memory persists everywhere",),
            ("🔍 Access from any AI",),
            ("🔄 AI remembers everything",),
            ("🚀 15-minute integration",),
        ]
        
        for i, (feature,) in enumerate(feature_list):
            feature_card = self.create_feature_card(feature)
            if i < 2:
                x_pos = -4.5
                y_pos = -0.2 - i * 1.8
            else:
                x_pos = 4.5
                y_pos = -0.2 - (i-2) * 1.8
            feature_card.move_to([x_pos, y_pos, 0])
            feature_highlights.add(feature_card)
        
        self.play(LaggedStartMap(FadeIn, feature_highlights, lag_ratio=0.2), run_time=1.5)
        
        summary_text = Text("Cilow saves memories once, retrieves them anywhere", 
                          font_size=14, color=GREEN, weight=BOLD)
        summary_text.move_to([0, -3.5, 0])
        self.play(Write(summary_text), run_time=0.8)
        
        self.wait(2)
        
        self.play(
            FadeOut(main_title),
            FadeOut(sub_title),
            FadeOut(cilow_hub),
            FadeOut(ai_platforms),
            FadeOut(connection_lines),
            FadeOut(feature_highlights),
            FadeOut(summary_text),
            run_time=1.2
        )

    def create_feature_card(self, text):
        card = RoundedRectangle(
            height=1.0, width=3.8,
            fill_color="#1e293b", fill_opacity=1,
            stroke_color="#8b5cf6", stroke_width=2,
            corner_radius=0.2
        )
        
        feature_text = Text(text, font_size=13, color=WHITE, weight=BOLD)
        feature_text.move_to(card.get_center())
        feature_text.set_width(card.width * 0.8)
        
        return VGroup(card, feature_text)

    def create_memory_hub(self):
        hub_container = RoundedRectangle(
            height=2.3, width=3.2,
            fill_color="#1e293b", fill_opacity=1,
            stroke_color="#8b5cf6", stroke_width=4,
            corner_radius=0.3
        )
        
        hub_title = Text("CILOW MEMORY", font_size=16, color="#8b5cf6", weight=BOLD)
        hub_title.move_to(hub_container.get_center() + UP * 0.8)
        
        memory_layers = VGroup()
        
        hot_layer = RoundedRectangle(
            height=0.35, width=2.5,
            fill_color="#ef4444", fill_opacity=0.8,
            stroke_width=0, corner_radius=0.1
        )
        hot_layer.move_to(hub_container.get_center() + UP * 0.15)
        hot_label = Text("🔥 HOT", font_size=7, color=WHITE, weight=BOLD)
        hot_label.move_to(hot_layer.get_center())
        
        warm_layer = RoundedRectangle(
            height=0.35, width=2.5,
            fill_color="#f59e0b", fill_opacity=0.8,
            stroke_width=0, corner_radius=0.1
        )
        warm_layer.move_to(hub_container.get_center() + DOWN * 0.25)
        warm_label = Text("🌤️ WARM", font_size=7, color=WHITE, weight=BOLD)
        warm_label.move_to(warm_layer.get_center())
        
        cold_layer = RoundedRectangle(
            height=0.35, width=2.5,
            fill_color="#3b82f6", fill_opacity=0.8,
            stroke_width=0, corner_radius=0.1
        )
        cold_layer.move_to(hub_container.get_center() + DOWN * 0.65)
        cold_label = Text("❄️ COLD", font_size=7, color=WHITE, weight=BOLD)
        cold_label.move_to(cold_layer.get_center())
        
        memory_layers.add(hot_layer, hot_label, warm_layer, warm_label, cold_layer, cold_label)
        
        return VGroup(hub_container, hub_title, memory_layers)

    def create_platform_badge(self, name, icon, color):
        badge = VGroup()
        
        base_circle = Circle(radius=0.5, fill_color=color, fill_opacity=0.15,
                     stroke_color=color, stroke_width=2)
        
        icon_symbol = Text(icon, font_size=16)
        icon_symbol.move_to(base_circle.get_center())
        
        name_label = Text(name, font_size=9, color=color, weight=BOLD)
        name_label.next_to(base_circle, DOWN, buff=0.15)
        
        badge.add(base_circle, icon_symbol, name_label)
        return badge

    def show_multi_platform_demo(self):
        demo_title = Text("Cilow in Action: Memory Across Platforms", font_size=26, color=WHITE, weight=BOLD)
        demo_title.to_edge(UP, buff=0.8)
        
        demo_subtitle = Text("Seamless context sharing across all AI Agents", font_size=14, color=GRAY_B)
        demo_subtitle.next_to(demo_title, DOWN, buff=0.1)
        
        self.play(Write(demo_title), FadeIn(demo_subtitle), run_time=0.8)
        
        chatgpt_demo = self.create_chat_window("ChatGPT", "#74aa9c")
        chatgpt_demo.move_to(LEFT * 4.8)
        
        claude_demo = self.create_chat_window("Claude", "#ff6b35")
        claude_demo.move_to(RIGHT * 0)
        
        gemini_demo = self.create_chat_window("Gemini", "#8a2be2")
        gemini_demo.move_to(RIGHT * 4.8)
        
        memory_dashboard = self.create_memory_dashboard()
        memory_dashboard.move_to([0, -3.0, 0])
        
        self.play(
            FadeIn(chatgpt_demo),
            FadeIn(claude_demo),
            FadeIn(gemini_demo),
            FadeIn(memory_dashboard),
            run_time=1.5
        )
        
        self.wait(0.5)
        
        chatgpt_query = self.create_chat_bubble("Our project deadline is next Friday. We need to complete all features by then.", True)
        chatgpt_query.move_to(chatgpt_demo[4].get_center() + UP * 0.6)
        
        chatgpt_reply = self.create_chat_bubble("Noted: Project deadline next Friday. Saved to Cilow memory! ✅", False)
        chatgpt_reply.move_to(chatgpt_demo[4].get_center() + DOWN * 0.3)
        
        self.play(FadeIn(chatgpt_query), run_time=0.6)
        self.wait(0.3)
        self.play(FadeIn(chatgpt_reply), run_time=0.6)
        
        save_notice = Text("💾 Saving to Memory", font_size=12, color=GREEN, weight=BOLD)
        save_notice.move_to([0, -1.8, 0])
        self.play(Write(save_notice), run_time=0.4)
        self.animate_data_save(chatgpt_demo, memory_dashboard, "hot")
        self.play(FadeOut(save_notice), run_time=0.3)
        
        self.wait(0.5)
        
        claude_query = self.create_chat_bubble("Can you help me plan this week's tasks?", True)
        claude_query.move_to(claude_demo[4].get_center() + UP * 0.6)
        self.play(FadeIn(claude_query), run_time=0.6)
        
        retrieve_notice = Text("🔍 Retrieving from Memory", font_size=12, color=BLUE, weight=BOLD)
        retrieve_notice.move_to([0, -1.8, 0])
        self.play(Write(retrieve_notice), run_time=0.4)
        self.animate_data_retrieve(memory_dashboard, claude_demo, "hot")
        
        claude_reply = self.create_chat_bubble("With Friday's deadline, let's prioritize critical features first! 📅", False)
        claude_reply.move_to(claude_demo[4].get_center() + DOWN * 0.3)
        self.play(FadeIn(claude_reply), run_time=0.6)
        self.play(FadeOut(retrieve_notice), run_time=0.3)
        
        self.wait(0.5)
        
        gemini_query = self.create_chat_bubble("What's our current project timeline?", True)
        gemini_query.move_to(gemini_demo[4].get_center() + UP * 0.6)
        self.play(FadeIn(gemini_query), run_time=0.6)
        
        self.animate_data_retrieve(memory_dashboard, gemini_demo, "hot")
        
        gemini_reply = self.create_chat_bubble("Project deadline: Next Friday. All features due by then. From Cilow memory! 🧠", False)
        gemini_reply.move_to(gemini_demo[4].get_center() + DOWN * 0.3)
        self.play(FadeIn(gemini_reply), run_time=0.6)
        
        success_message = Text("✓ Memory works across all platforms & agents ✓ No repetition needed ✓ Context always available", 
                         font_size=11, color=GREEN, weight=BOLD)
        success_message.move_to([0, -4.2, 0])
        self.play(Write(success_message), run_time=0.8)
        
        self.wait(2)
        
        self.play(
            FadeOut(demo_title),
            FadeOut(demo_subtitle),
            FadeOut(chatgpt_demo),
            FadeOut(claude_demo),
            FadeOut(gemini_demo),
            FadeOut(memory_dashboard),
            FadeOut(chatgpt_query),
            FadeOut(chatgpt_reply),
            FadeOut(claude_query),
            FadeOut(claude_reply),
            FadeOut(gemini_query),
            FadeOut(gemini_reply),
            FadeOut(success_message),
            run_time=1.2
        )

    def create_memory_dashboard(self):
        dashboard = RoundedRectangle(
            height=1.6, width=8.5,
            fill_color="#1e293b", fill_opacity=1,
            stroke_color="#8b5cf6", stroke_width=3,
            corner_radius=0.3
        )
        
        dashboard_title = Text("Cilow Memory System", font_size=12, color="#8b5cf6", weight=BOLD)
        dashboard_title.move_to(dashboard.get_top() + DOWN * 0.3)
        
        memory_tiers = VGroup()
        
        hot_tier = RoundedRectangle(
            height=0.25, width=6.5,
            fill_color="#ef4444", fill_opacity=0.8,
            stroke_width=0, corner_radius=0.1
        )
        hot_tier.move_to(dashboard.get_center() + UP * 0.3)
        hot_label = Text("🔥 HOT", font_size=8, color=WHITE, weight=BOLD)
        hot_label.move_to(hot_tier.get_left() + RIGHT * 0.8)
        
        warm_tier = RoundedRectangle(
            height=0.25, width=6.5,
            fill_color="#f59e0b", fill_opacity=0.8,
            stroke_width=0, corner_radius=0.1
        )
        warm_tier.move_to(dashboard.get_center())
        warm_label = Text("🌤️ WARM", font_size=8, color=WHITE, weight=BOLD)
        warm_label.move_to(warm_tier.get_left() + RIGHT * 0.8)
        
        cold_tier = RoundedRectangle(
            height=0.25, width=6.5,
            fill_color="#3b82f6", fill_opacity=0.8,
            stroke_width=0, corner_radius=0.1
        )
        cold_tier.move_to(dashboard.get_center() + DOWN * 0.3)
        cold_label = Text("❄️ COLD", font_size=8, color=WHITE, weight=BOLD)
        cold_label.move_to(cold_tier.get_left() + RIGHT * 0.8)
        
        memory_tiers.add(hot_tier, hot_label, warm_tier, warm_label, cold_tier, cold_label)
        
        status_indicator = Text("Active • Synced • Encrypted", font_size=8, color=GREEN)
        status_indicator.move_to(dashboard.get_center() + DOWN * 0.7)
        
        return VGroup(dashboard, dashboard_title, memory_tiers, status_indicator)

    def animate_data_save(self, source, target, tier_type):
        if tier_type == "hot":
            target_position = target[2][0].get_center()
        elif tier_type == "warm":
            target_position = target[2][2].get_center()
        else:
            target_position = target[2][4].get_center()
        
        connection_path = CurvedArrow(
            source[0].get_center(), 
            target_position,
            color=GREEN, 
            stroke_width=2,
            angle=-0.2
        )
        
        data_packet = Text("💾", font_size=10)
        data_packet.set_color(GREEN)
        data_packet.move_to(connection_path.get_start())
        
        self.play(Create(connection_path), run_time=0.4)
        self.play(FadeIn(data_packet), run_time=0.2)
        self.play(
            data_packet.animate.move_to(connection_path.get_end()),
            run_time=1.0
        )
        
        self.play(
            FadeOut(connection_path),
            FadeOut(data_packet),
            run_time=0.3
        )

    def animate_data_retrieve(self, source, target, tier_type):
        if tier_type == "hot":
            source_position = source[2][0].get_center()
        elif tier_type == "warm":
            source_position = source[2][2].get_center()
        else:
            source_position = source[2][4].get_center()
        
        connection_path = CurvedArrow(
            source_position,
            target[0].get_center(),
            color=BLUE,
            stroke_width=2,
            angle=0.2
        )
        
        data_packet = Text("🔍", font_size=10)
        data_packet.set_color(BLUE)
        data_packet.move_to(connection_path.get_start())
        
        self.play(Create(connection_path), run_time=0.4)
        self.play(FadeIn(data_packet), run_time=0.2)
        self.play(
            data_packet.animate.move_to(connection_path.get_end()),
            run_time=1.0
        )
        
        self.play(
            FadeOut(connection_path),
            FadeOut(data_packet),
            run_time=0.3
        )

    def create_final_call_to_action(self):
        self.clear()
        
        logo_circle = Circle(radius=1.0, stroke_color="#6366f1", stroke_width=5, fill_opacity=0)
        brain_symbol = Text("🧠", font_size=50)
        brain_symbol.move_to(logo_circle.get_center())
        
        brand_name = Text("CILOW", font_size=56, weight=BOLD)
        brand_name.set_color_by_gradient("#6366f1", "#8b5cf6")
        brand_name.move_to(UP * 2.5)
        
        tagline = Text("Persistent Memory for AI Agents", font_size=20, color=GRAY_B)
        tagline.next_to(brand_name, DOWN, buff=0.2)
        
        feature_cards = VGroup()
        feature_points = [
            "Works with any LLM & agent",
            "Remember across all platforms", 
            "Access from any AI",
            "15-minute integration",
        ]
        
        for i, point in enumerate(feature_points):
            feature_card = self.create_feature_highlight(point)
            if i < 2:
                x_pos = -4.5
                y_pos = 0.8 - i * 1.8
            else:
                x_pos = 4.5
                y_pos = 0.8 - (i-2) * 1.8
            feature_card.move_to([x_pos, y_pos, 0])
            feature_cards.add(feature_card)
        
        action_button = RoundedRectangle(
            height=0.9, width=6.5,
            fill_color="#6366f1", fill_opacity=1,
            stroke_color="#8b5cf6", stroke_width=3,
            corner_radius=0.4
        )
        action_button.move_to([0, -2.5, 0])
        
        button_text = Text("Start Building with Persistent AI Memory", font_size=16, color=WHITE, weight=BOLD)
        button_text.move_to(action_button.get_center())
        
        website_url = Text("cilow.ai", font_size=14, color="#8b5cf6", weight=BOLD)
        website_url.next_to(action_button, DOWN, buff=0.4)
        
        platform_note = Text("Works across all AI Agents", font_size=10, color=GRAY_B)
        platform_note.next_to(website_url, DOWN, buff=0.2)
        
        self.play(DrawBorderThenFill(logo_circle), FadeIn(brain_symbol), run_time=1)
        self.play(DrawBorderThenFill(brand_name), Write(tagline), run_time=1.2)
        self.play(LaggedStartMap(FadeIn, feature_cards, lag_ratio=0.15), run_time=1.5)
        self.play(GrowFromCenter(action_button), run_time=0.8)
        self.play(Write(button_text), run_time=0.6)
        self.play(Write(website_url), Write(platform_note), run_time=0.4)
        
        self.play(
            action_button.animate.set_fill(opacity=0.9),
            button_text.animate.scale(1.05),
            run_time=1,
            rate_func=there_and_back
        )
        
        self.wait(3)

    def create_feature_highlight(self, description):
        card_frame = RoundedRectangle(
            height=1.0, width=4.0,
            fill_color="#1e293b", fill_opacity=1,
            stroke_color="#8b5cf6", stroke_width=2,
            corner_radius=0.2
        )
        
        description_text = Text(description, font_size=14, color=WHITE, weight=BOLD)
        description_text.move_to(card_frame.get_center())
        description_text.set_width(card_frame.width * 0.8)
        
        return VGroup(card_frame, description_text)

if __name__ == "__main__":
    scene = AI_Memory_Solution_Video()
    scene.render()