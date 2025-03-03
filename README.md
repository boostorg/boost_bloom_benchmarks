### GCC 14, x64
<!--gcc-x64/comparison_table.cpp.txt-->
#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">25.73</td>
    <td align="right">4.36</td>
    <td align="right">3.54</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">10.38</td>
    <td align="right">9.85</td>
    <td align="right">15.92</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">3.75</td>
    <td align="right">3.91</td>
    <td align="right">4.01</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">5.63</td>
    <td align="right">5.04</td>
    <td align="right">5.06</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">16.17</td>
    <td align="right">14.20</td>
    <td align="right">16.57</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">4.48</td>
    <td align="right">4.50</td>
    <td align="right">4.51</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">6.57</td>
    <td align="right">7.72</td>
    <td align="right">7.73</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">19.35</td>
    <td align="right">17.97</td>
    <td align="right">15.93</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">5.14</td>
    <td align="right">5.06</td>
    <td align="right">5.18</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">9.66</td>
    <td align="right">12.48</td>
    <td align="right">12.46</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">26.03</td>
    <td align="right">22.98</td>
    <td align="right">16.41</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">5.97</td>
    <td align="right">5.84</td>
    <td align="right">5.73</td>
    <td align="center">14</td>
    <td align="right">0.0163</td>
    <td align="right">11.75</td>
    <td align="right">14.93</td>
    <td align="right">14.95</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7421</td>
    <td align="right">8.02</td>
    <td align="right">10.93</td>
    <td align="right">10.84</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">4.51</td>
    <td align="right">4.70</td>
    <td align="right">4.69</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">5.73</td>
    <td align="right">5.38</td>
    <td align="right">5.39</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5384</td>
    <td align="right">3.43</td>
    <td align="right">4.42</td>
    <td align="right">4.42</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">5.06</td>
    <td align="right">5.18</td>
    <td align="right">5.11</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">12.23</td>
    <td align="right">8.52</td>
    <td align="right">8.51</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1163</td>
    <td align="right">17.30</td>
    <td align="right">10.54</td>
    <td align="right">8.35</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">5.92</td>
    <td align="right">5.93</td>
    <td align="right">5.93</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">10.76</td>
    <td align="right">11.23</td>
    <td align="right">11.23</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0286</td>
    <td align="right">9.20</td>
    <td align="right">10.64</td>
    <td align="right">5.91</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">6.41</td>
    <td align="right">6.37</td>
    <td align="right">6.38</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">12.97</td>
    <td align="right">14.18</td>
    <td align="right">14.15</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">30.75</td>
    <td align="right">18.21</td>
    <td align="right">6.63</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">13.72</td>
    <td align="right">13.31</td>
    <td align="right">17.68</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">4.80</td>
    <td align="right">4.97</td>
    <td align="right">5.07</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">7.15</td>
    <td align="right">6.89</td>
    <td align="right">6.94</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">20.28</td>
    <td align="right">19.85</td>
    <td align="right">18.39</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">5.79</td>
    <td align="right">6.66</td>
    <td align="right">5.81</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">8.13</td>
    <td align="right">10.09</td>
    <td align="right">10.17</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">26.88</td>
    <td align="right">26.82</td>
    <td align="right">19.21</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">7.27</td>
    <td align="right">9.01</td>
    <td align="right">7.05</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">12.52</td>
    <td align="right">17.23</td>
    <td align="right">18.14</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">54.30</td>
    <td align="right">44.06</td>
    <td align="right">19.82</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">10.24</td>
    <td align="right">10.84</td>
    <td align="right">10.59</td>
    <td align="center">14</td>
    <td align="right">0.0153</td>
    <td align="right">18.50</td>
    <td align="right">21.78</td>
    <td align="right">22.60</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7269</td>
    <td align="right">8.17</td>
    <td align="right">10.72</td>
    <td align="right">10.72</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">5.86</td>
    <td align="right">5.98</td>
    <td align="right">5.98</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">7.62</td>
    <td align="right">6.75</td>
    <td align="right">6.71</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5394</td>
    <td align="right">4.34</td>
    <td align="right">6.02</td>
    <td align="right">5.58</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">6.31</td>
    <td align="right">6.22</td>
    <td align="right">6.25</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">12.68</td>
    <td align="right">13.81</td>
    <td align="right">9.67</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1161</td>
    <td align="right">18.03</td>
    <td align="right">12.62</td>
    <td align="right">11.10</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">8.76</td>
    <td align="right">7.72</td>
    <td align="right">7.84</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">12.59</td>
    <td align="right">13.11</td>
    <td align="right">13.32</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0287</td>
    <td align="right">16.08</td>
    <td align="right">20.98</td>
    <td align="right">10.70</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">10.39</td>
    <td align="right">10.13</td>
    <td align="right">10.74</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">18.48</td>
    <td align="right">26.17</td>
    <td align="right">22.05</td>
  </tr>
</table>

<!--gcc-x64/comparison_table.cpp.txt-->

### Clang 18, X64
<!--clang-x64/comparison_table.cpp.txt-->
#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">27.50</td>
    <td align="right">5.35</td>
    <td align="right">3.86</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">9.30</td>
    <td align="right">8.89</td>
    <td align="right">15.42</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">3.32</td>
    <td align="right">3.94</td>
    <td align="right">4.09</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">5.84</td>
    <td align="right">6.03</td>
    <td align="right">6.26</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">13.24</td>
    <td align="right">14.32</td>
    <td align="right">17.00</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">3.93</td>
    <td align="right">4.57</td>
    <td align="right">4.59</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">8.91</td>
    <td align="right">9.23</td>
    <td align="right">9.23</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">17.47</td>
    <td align="right">16.85</td>
    <td align="right">15.88</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">4.43</td>
    <td align="right">5.13</td>
    <td align="right">5.11</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">10.68</td>
    <td align="right">13.46</td>
    <td align="right">13.45</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">20.38</td>
    <td align="right">21.11</td>
    <td align="right">16.18</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">4.90</td>
    <td align="right">5.78</td>
    <td align="right">5.93</td>
    <td align="center">14</td>
    <td align="right">0.0163</td>
    <td align="right">14.59</td>
    <td align="right">14.08</td>
    <td align="right">14.11</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7421</td>
    <td align="right">3.60</td>
    <td align="right">4.26</td>
    <td align="right">4.24</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">3.89</td>
    <td align="right">4.62</td>
    <td align="right">4.64</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">5.12</td>
    <td align="right">5.90</td>
    <td align="right">5.94</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5384</td>
    <td align="right">2.94</td>
    <td align="right">3.77</td>
    <td align="right">3.76</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">4.55</td>
    <td align="right">5.52</td>
    <td align="right">5.46</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">7.76</td>
    <td align="right">9.64</td>
    <td align="right">9.39</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1163</td>
    <td align="right">10.67</td>
    <td align="right">6.28</td>
    <td align="right">4.82</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">4.94</td>
    <td align="right">5.99</td>
    <td align="right">6.01</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">11.07</td>
    <td align="right">14.09</td>
    <td align="right">12.88</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0286</td>
    <td align="right">6.15</td>
    <td align="right">6.99</td>
    <td align="right">4.61</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">5.49</td>
    <td align="right">6.49</td>
    <td align="right">6.50</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">15.13</td>
    <td align="right">15.36</td>
    <td align="right">15.39</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">38.63</td>
    <td align="right">18.67</td>
    <td align="right">9.01</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">11.65</td>
    <td align="right">11.27</td>
    <td align="right">16.72</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">4.14</td>
    <td align="right">4.80</td>
    <td align="right">4.78</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">7.16</td>
    <td align="right">7.41</td>
    <td align="right">7.72</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">17.05</td>
    <td align="right">17.56</td>
    <td align="right">18.00</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">5.07</td>
    <td align="right">6.39</td>
    <td align="right">6.89</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">12.14</td>
    <td align="right">11.06</td>
    <td align="right">10.52</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">21.45</td>
    <td align="right">22.11</td>
    <td align="right">16.66</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">5.42</td>
    <td align="right">6.16</td>
    <td align="right">6.14</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">12.66</td>
    <td align="right">15.28</td>
    <td align="right">15.29</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">32.60</td>
    <td align="right">34.72</td>
    <td align="right">17.76</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">7.46</td>
    <td align="right">8.71</td>
    <td align="right">8.63</td>
    <td align="center">14</td>
    <td align="right">0.0153</td>
    <td align="right">17.56</td>
    <td align="right">17.42</td>
    <td align="right">17.24</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7269</td>
    <td align="right">4.31</td>
    <td align="right">5.11</td>
    <td align="right">5.07</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">4.23</td>
    <td align="right">4.92</td>
    <td align="right">4.93</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">6.07</td>
    <td align="right">7.16</td>
    <td align="right">7.17</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5394</td>
    <td align="right">3.44</td>
    <td align="right">4.32</td>
    <td align="right">4.31</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">4.68</td>
    <td align="right">5.40</td>
    <td align="right">5.19</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">8.56</td>
    <td align="right">10.80</td>
    <td align="right">10.72</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1161</td>
    <td align="right">11.38</td>
    <td align="right">8.39</td>
    <td align="right">6.31</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">6.18</td>
    <td align="right">7.18</td>
    <td align="right">7.17</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">12.87</td>
    <td align="right">16.42</td>
    <td align="right">14.83</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0287</td>
    <td align="right">10.02</td>
    <td align="right">11.45</td>
    <td align="right">7.82</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">7.80</td>
    <td align="right">9.34</td>
    <td align="right">8.91</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">23.08</td>
    <td align="right">19.99</td>
    <td align="right">21.38</td>
  </tr>
</table>

<!--clang-x64/comparison_table.cpp.txt-->

### Clang 15, ARM64
<!--clang-arm64/comparison_table.cpp.txt-->
#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">21.62</td>
    <td align="right">4.04</td>
    <td align="right">3.20</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">7.32</td>
    <td align="right">4.83</td>
    <td align="right">12.41</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">1.42</td>
    <td align="right">1.30</td>
    <td align="right">1.30</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">2.38</td>
    <td align="right">1.94</td>
    <td align="right">1.97</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">11.59</td>
    <td align="right">7.55</td>
    <td align="right">12.84</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">1.46</td>
    <td align="right">1.44</td>
    <td align="right">1.45</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.47</td>
    <td align="right">2.44</td>
    <td align="right">2.42</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">15.15</td>
    <td align="right">11.28</td>
    <td align="right">12.96</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">1.60</td>
    <td align="right">1.71</td>
    <td align="right">1.60</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">5.59</td>
    <td align="right">3.20</td>
    <td align="right">3.03</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">18.85</td>
    <td align="right">12.40</td>
    <td align="right">12.66</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">1.84</td>
    <td align="right">2.66</td>
    <td align="right">2.54</td>
    <td align="center">14</td>
    <td align="right">0.0163</td>
    <td align="right">5.14</td>
    <td align="right">4.13</td>
    <td align="right">3.64</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.18</td>
    <td align="right">1.99</td>
    <td align="right">2.04</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">1.72</td>
    <td align="right">1.37</td>
    <td align="right">1.32</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">2.47</td>
    <td align="right">1.91</td>
    <td align="right">1.90</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">1.63</td>
    <td align="right">1.50</td>
    <td align="right">1.54</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">1.81</td>
    <td align="right">1.56</td>
    <td align="right">1.55</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.07</td>
    <td align="right">2.43</td>
    <td align="right">2.37</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">3.15</td>
    <td align="right">3.00</td>
    <td align="right">2.28</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">1.83</td>
    <td align="right">1.70</td>
    <td align="right">1.74</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">4.54</td>
    <td align="right">3.28</td>
    <td align="right">3.23</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0304</td>
    <td align="right">3.34</td>
    <td align="right">3.42</td>
    <td align="right">2.26</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">1.97</td>
    <td align="right">1.76</td>
    <td align="right">1.77</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">5.24</td>
    <td align="right">4.22</td>
    <td align="right">4.31</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">28.68</td>
    <td align="right">13.26</td>
    <td align="right">8.53</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">9.30</td>
    <td align="right">10.99</td>
    <td align="right">19.07</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">3.09</td>
    <td align="right">3.20</td>
    <td align="right">3.82</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">3.80</td>
    <td align="right">4.31</td>
    <td align="right">3.74</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">24.39</td>
    <td align="right">21.18</td>
    <td align="right">21.62</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">6.73</td>
    <td align="right">5.21</td>
    <td align="right">7.00</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">7.51</td>
    <td align="right">8.19</td>
    <td align="right">8.80</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">46.98</td>
    <td align="right">37.28</td>
    <td align="right">22.92</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">9.49</td>
    <td align="right">8.18</td>
    <td align="right">8.20</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">16.57</td>
    <td align="right">12.90</td>
    <td align="right">12.86</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">69.20</td>
    <td align="right">50.74</td>
    <td align="right">25.82</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">11.93</td>
    <td align="right">9.49</td>
    <td align="right">8.72</td>
    <td align="center">14</td>
    <td align="right">0.0153</td>
    <td align="right">19.88</td>
    <td align="right">18.25</td>
    <td align="right">17.71</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.79</td>
    <td align="right">4.79</td>
    <td align="right">4.72</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">2.85</td>
    <td align="right">2.97</td>
    <td align="right">2.04</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">3.31</td>
    <td align="right">4.68</td>
    <td align="right">4.53</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">5.26</td>
    <td align="right">6.71</td>
    <td align="right">6.52</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">6.48</td>
    <td align="right">5.45</td>
    <td align="right">6.06</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">7.75</td>
    <td align="right">7.96</td>
    <td align="right">7.19</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">10.15</td>
    <td align="right">12.12</td>
    <td align="right">9.98</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">9.46</td>
    <td align="right">7.41</td>
    <td align="right">8.69</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">15.63</td>
    <td align="right">13.49</td>
    <td align="right">14.38</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0276</td>
    <td align="right">13.42</td>
    <td align="right">14.88</td>
    <td align="right">7.75</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">8.99</td>
    <td align="right">6.37</td>
    <td align="right">8.72</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">21.47</td>
    <td align="right">19.07</td>
    <td align="right">18.25</td>
  </tr>
</table>

<!--clang-arm64/comparison_table.cpp.txt-->

### VS 2022, x64
<!--vs-x64/comparison_table.cpp.txt-->
<!--vs-x64/comparison_table.cpp.txt-->
