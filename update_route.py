path = 'index.html'
with open(path, encoding='utf-8') as f:
    html = f.read()

old = """  <div class="card">
    <div class="card-title">🚃 出発当日 — 東戸塚からのアクセス（AF便）</div>
    <div class="route-card">
      <div class="route-title">🥇 エールフランス — 羽田空港 T3（08:50発）チェックイン締切 07:50</div>
      <div class="route-step"><span class="route-time">05:05頃</span><span><strong>東戸塚駅</strong> 出発（横須賀線 上り・<strong>初電</strong>）</span></div>
      <div class="route-arrow">↓ 横須賀線 約8分</div>
      <div class="route-step"><span class="route-time">05:13頃</span><span><strong>横浜駅</strong> 乗換 → 京急本線（羽田空港方面）<br><small style="color:var(--gray-600)">横浜で京急ホームへ移動（約5分）。始発またはエアポート急行を利用</small></span></div>
      <div class="route-arrow">↓ 京急 約28分</div>
      <div class="route-step"><span class="route-time">05:45頃</span><span><strong>羽田空港第3ターミナル</strong> 到着<br><small style="color:var(--gray-600)">チェックイン締切 07:50 まで2時間以上の余裕あり ✅</small></span></div>
      <div class="info gold" style="margin-top:12px;margin-bottom:0">💡 京急は Suica・PASMO でそのまま乗れます。横浜〜羽田T3 は約 ¥370。余裕を持つなら <strong>05:57頃発</strong>（1本早い電車）が安心。</div>
    </div>
  </div>"""

new = """  <div class="card">
    <div class="card-title">🚃 出発当日 — 東戸塚からのアクセス（AF便）</div>
    <div class="route-card">
      <div class="route-title">🥇 エールフランス — 羽田空港 T3（08:50発）チェックイン締切 07:50</div>
      <div class="route-step"><span class="route-time">05:31</span><span><strong>東戸塚駅</strong> 発（JR横須賀線・1番線 / 15両編成）</span></div>
      <div class="route-arrow">↓ JR横須賀線 約7分</div>
      <div class="route-step"><span class="route-time">05:38</span><span><strong>横浜駅</strong> 着 → 乗換</span></div>
      <div class="route-arrow">↓ 徒歩 ホーム移動</div>
      <div class="route-step"><span class="route-time">05:59</span><span><strong>横浜駅</strong> 発（京急本線急行・2番線）<br><small style="color:var(--gray-600)">京急蒲田 乗換不要 → そのまま京急空港線急行へ</small></span></div>
      <div class="route-arrow">↓ 京急 約25分</div>
      <div class="route-step"><span class="route-time">06:24</span><span><strong>羽田空港第3ターミナル（京急）</strong> 着<br><small style="color:var(--gray-600)">改札出口2 → 徒歩5分</small></span></div>
      <div class="route-arrow">↓ 徒歩 約5分</div>
      <div class="route-step"><span class="route-time">06:31</span><span><strong>羽田空港 第3ターミナル</strong> 到着<br><small style="color:var(--gray-600)">チェックイン締切 07:50 まで約1時間20分の余裕あり ✅</small></span></div>
      <div class="info gold" style="margin-top:12px;margin-bottom:0">💡 IC優先（Suica・PASMO）。横浜〜羽田T3 は定期代＋363円。乗換1回・26.9km</div>
    </div>
  </div>"""

assert old in html, "❌ 対象文字列が見つかりません"
html = html.replace(old, new, 1)
with open(path, 'w', encoding='utf-8') as f:
    f.write(html)
print("✅ 更新完了")
