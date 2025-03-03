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
    <td align="right">25.88</td>
    <td align="right">4.38</td>
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
    <td align="right">11.02</td>
    <td align="right">10.47</td>
    <td align="right">16.49</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">3.95</td>
    <td align="right">4.12</td>
    <td align="right">4.23</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">5.91</td>
    <td align="right">5.55</td>
    <td align="right">5.55</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">16.58</td>
    <td align="right">15.50</td>
    <td align="right">17.40</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">4.85</td>
    <td align="right">4.86</td>
    <td align="right">4.86</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">7.02</td>
    <td align="right">8.86</td>
    <td align="right">8.85</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">20.49</td>
    <td align="right">18.64</td>
    <td align="right">16.43</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">5.43</td>
    <td align="right">5.33</td>
    <td align="right">5.45</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">10.13</td>
    <td align="right">13.80</td>
    <td align="right">13.78</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">26.96</td>
    <td align="right">24.10</td>
    <td align="right">16.74</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">6.18</td>
    <td align="right">6.08</td>
    <td align="right">5.91</td>
    <td align="center">14</td>
    <td align="right">0.0163</td>
    <td align="right">12.27</td>
    <td align="right">15.79</td>
    <td align="right">15.79</td>
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
    <td align="right">8.01</td>
    <td align="right">10.56</td>
    <td align="right">10.59</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">4.85</td>
    <td align="right">5.03</td>
    <td align="right">5.03</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">6.14</td>
    <td align="right">5.71</td>
    <td align="right">5.69</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5384</td>
    <td align="right">3.70</td>
    <td align="right">4.77</td>
    <td align="right">4.76</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">5.40</td>
    <td align="right">5.52</td>
    <td align="right">5.53</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">11.73</td>
    <td align="right">9.03</td>
    <td align="right">9.04</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1163</td>
    <td align="right">17.14</td>
    <td align="right">10.46</td>
    <td align="right">8.29</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">6.21</td>
    <td align="right">6.25</td>
    <td align="right">6.25</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">11.16</td>
    <td align="right">11.68</td>
    <td align="right">11.69</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0286</td>
    <td align="right">9.05</td>
    <td align="right">10.56</td>
    <td align="right">6.07</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">6.65</td>
    <td align="right">6.62</td>
    <td align="right">6.64</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">13.40</td>
    <td align="right">14.63</td>
    <td align="right">14.61</td>
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
    <td align="right">29.58</td>
    <td align="right">17.45</td>
    <td align="right">6.40</td>
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
    <td align="right">13.27</td>
    <td align="right">12.55</td>
    <td align="right">17.46</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">4.72</td>
    <td align="right">4.92</td>
    <td align="right">4.99</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">7.04</td>
    <td align="right">6.79</td>
    <td align="right">6.77</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">19.09</td>
    <td align="right">17.68</td>
    <td align="right">17.80</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">5.32</td>
    <td align="right">5.28</td>
    <td align="right">5.32</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">7.66</td>
    <td align="right">9.49</td>
    <td align="right">9.48</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">24.36</td>
    <td align="right">22.55</td>
    <td align="right">17.16</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">6.28</td>
    <td align="right">6.14</td>
    <td align="right">6.25</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">11.65</td>
    <td align="right">14.75</td>
    <td align="right">14.81</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">36.55</td>
    <td align="right">33.72</td>
    <td align="right">17.98</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">7.99</td>
    <td align="right">8.07</td>
    <td align="right">8.19</td>
    <td align="center">14</td>
    <td align="right">0.0153</td>
    <td align="right">15.45</td>
    <td align="right">18.31</td>
    <td align="right">18.21</td>
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
    <td align="right">8.16</td>
    <td align="right">10.70</td>
    <td align="right">10.72</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">5.56</td>
    <td align="right">5.71</td>
    <td align="right">5.71</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">7.08</td>
    <td align="right">6.52</td>
    <td align="right">6.49</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5394</td>
    <td align="right">4.18</td>
    <td align="right">5.29</td>
    <td align="right">5.31</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">5.99</td>
    <td align="right">5.99</td>
    <td align="right">5.99</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">12.58</td>
    <td align="right">9.80</td>
    <td align="right">9.82</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1161</td>
    <td align="right">17.64</td>
    <td align="right">10.89</td>
    <td align="right">8.78</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">7.17</td>
    <td align="right">7.12</td>
    <td align="right">7.20</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">12.78</td>
    <td align="right">13.01</td>
    <td align="right">13.06</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0287</td>
    <td align="right">11.99</td>
    <td align="right">12.99</td>
    <td align="right">8.31</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">8.81</td>
    <td align="right">8.60</td>
    <td align="right">8.60</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">16.68</td>
    <td align="right">17.90</td>
    <td align="right">17.24</td>
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
    <td align="right">26.99</td>
    <td align="right">4.47</td>
    <td align="right">3.42</td>
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
    <td align="right">9.17</td>
    <td align="right">8.83</td>
    <td align="right">15.33</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">3.31</td>
    <td align="right">3.94</td>
    <td align="right">3.93</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">5.78</td>
    <td align="right">5.97</td>
    <td align="right">6.20</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">13.07</td>
    <td align="right">14.21</td>
    <td align="right">16.77</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">3.83</td>
    <td align="right">4.55</td>
    <td align="right">4.56</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">8.80</td>
    <td align="right">9.14</td>
    <td align="right">9.15</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">17.12</td>
    <td align="right">16.35</td>
    <td align="right">15.63</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">4.33</td>
    <td align="right">5.09</td>
    <td align="right">5.06</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">10.60</td>
    <td align="right">13.40</td>
    <td align="right">13.42</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">20.04</td>
    <td align="right">20.41</td>
    <td align="right">15.96</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">4.79</td>
    <td align="right">5.66</td>
    <td align="right">5.86</td>
    <td align="center">14</td>
    <td align="right">0.0163</td>
    <td align="right">14.24</td>
    <td align="right">13.85</td>
    <td align="right">13.83</td>
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
    <td align="right">3.49</td>
    <td align="right">4.18</td>
    <td align="right">4.17</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">3.86</td>
    <td align="right">4.55</td>
    <td align="right">4.56</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">5.05</td>
    <td align="right">5.84</td>
    <td align="right">5.84</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5384</td>
    <td align="right">2.88</td>
    <td align="right">3.72</td>
    <td align="right">3.70</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">4.49</td>
    <td align="right">5.49</td>
    <td align="right">5.29</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">7.55</td>
    <td align="right">9.31</td>
    <td align="right">9.30</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1163</td>
    <td align="right">10.70</td>
    <td align="right">6.27</td>
    <td align="right">4.82</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">4.93</td>
    <td align="right">5.97</td>
    <td align="right">6.08</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">10.82</td>
    <td align="right">13.90</td>
    <td align="right">12.82</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0286</td>
    <td align="right">6.06</td>
    <td align="right">6.86</td>
    <td align="right">4.50</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">5.42</td>
    <td align="right">6.42</td>
    <td align="right">6.42</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">14.93</td>
    <td align="right">15.29</td>
    <td align="right">15.30</td>
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
    <td align="right">31.49</td>
    <td align="right">16.37</td>
    <td align="right">6.17</td>
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
    <td align="right">10.91</td>
    <td align="right">10.53</td>
    <td align="right">16.24</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">3.91</td>
    <td align="right">4.56</td>
    <td align="right">4.55</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">6.90</td>
    <td align="right">7.12</td>
    <td align="right">7.46</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">14.68</td>
    <td align="right">15.27</td>
    <td align="right">17.23</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">4.26</td>
    <td align="right">4.95</td>
    <td align="right">4.95</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">9.80</td>
    <td align="right">9.98</td>
    <td align="right">9.99</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">19.15</td>
    <td align="right">19.25</td>
    <td align="right">16.31</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">5.14</td>
    <td align="right">5.82</td>
    <td align="right">5.87</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">12.11</td>
    <td align="right">14.65</td>
    <td align="right">14.64</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">30.98</td>
    <td align="right">32.05</td>
    <td align="right">17.14</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">6.53</td>
    <td align="right">7.36</td>
    <td align="right">7.40</td>
    <td align="center">14</td>
    <td align="right">0.0153</td>
    <td align="right">15.98</td>
    <td align="right">15.80</td>
    <td align="right">15.78</td>
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
    <td align="right">4.19</td>
    <td align="right">4.95</td>
    <td align="right">4.93</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">4.58</td>
    <td align="right">5.30</td>
    <td align="right">5.31</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">6.00</td>
    <td align="right">7.01</td>
    <td align="right">7.02</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5394</td>
    <td align="right">3.33</td>
    <td align="right">4.18</td>
    <td align="right">4.16</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">5.07</td>
    <td align="right">5.97</td>
    <td align="right">5.82</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">8.23</td>
    <td align="right">10.33</td>
    <td align="right">10.31</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1161</td>
    <td align="right">10.94</td>
    <td align="right">7.47</td>
    <td align="right">5.78</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">5.86</td>
    <td align="right">6.86</td>
    <td align="right">7.03</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">12.24</td>
    <td align="right">15.58</td>
    <td align="right">14.29</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0287</td>
    <td align="right">8.53</td>
    <td align="right">9.67</td>
    <td align="right">6.73</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">7.66</td>
    <td align="right">9.15</td>
    <td align="right">10.04</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">20.30</td>
    <td align="right">19.15</td>
    <td align="right">18.23</td>
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
    <td align="right">21.00</td>
    <td align="right">4.25</td>
    <td align="right">3.42</td>
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
    <td align="right">7.46</td>
    <td align="right">5.05</td>
    <td align="right">12.43</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">1.41</td>
    <td align="right">1.32</td>
    <td align="right">1.27</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">2.51</td>
    <td align="right">1.85</td>
    <td align="right">1.89</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">11.88</td>
    <td align="right">7.48</td>
    <td align="right">12.93</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">1.45</td>
    <td align="right">4.14</td>
    <td align="right">1.54</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.38</td>
    <td align="right">2.14</td>
    <td align="right">2.18</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">13.09</td>
    <td align="right">9.97</td>
    <td align="right">12.27</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">1.79</td>
    <td align="right">1.77</td>
    <td align="right">1.67</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">4.22</td>
    <td align="right">3.15</td>
    <td align="right">3.16</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">19.02</td>
    <td align="right">12.02</td>
    <td align="right">12.44</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">1.91</td>
    <td align="right">2.14</td>
    <td align="right">2.12</td>
    <td align="center">14</td>
    <td align="right">0.0163</td>
    <td align="right">4.79</td>
    <td align="right">4.30</td>
    <td align="right">3.59</td>
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
    <td align="right">2.08</td>
    <td align="right">1.90</td>
    <td align="right">1.87</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">1.71</td>
    <td align="right">1.33</td>
    <td align="right">1.39</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">2.51</td>
    <td align="right">1.89</td>
    <td align="right">2.00</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">1.59</td>
    <td align="right">1.73</td>
    <td align="right">1.52</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">1.79</td>
    <td align="right">1.60</td>
    <td align="right">1.56</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.04</td>
    <td align="right">2.40</td>
    <td align="right">2.42</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">3.27</td>
    <td align="right">2.94</td>
    <td align="right">2.25</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">1.94</td>
    <td align="right">1.75</td>
    <td align="right">1.63</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">4.50</td>
    <td align="right">3.31</td>
    <td align="right">3.13</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0304</td>
    <td align="right">3.27</td>
    <td align="right">3.67</td>
    <td align="right">2.18</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">1.93</td>
    <td align="right">1.73</td>
    <td align="right">1.76</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">5.20</td>
    <td align="right">4.03</td>
    <td align="right">3.85</td>
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
    <td align="right">29.21</td>
    <td align="right">13.85</td>
    <td align="right">8.50</td>
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
    <td align="right">9.35</td>
    <td align="right">9.33</td>
    <td align="right">17.53</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">2.26</td>
    <td align="right">3.02</td>
    <td align="right">3.67</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">3.22</td>
    <td align="right">6.35</td>
    <td align="right">4.85</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">23.53</td>
    <td align="right">26.69</td>
    <td align="right">22.93</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">7.15</td>
    <td align="right">6.50</td>
    <td align="right">5.84</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">6.99</td>
    <td align="right">8.18</td>
    <td align="right">7.64</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">46.46</td>
    <td align="right">37.20</td>
    <td align="right">23.64</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">8.41</td>
    <td align="right">6.94</td>
    <td align="right">7.11</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">14.12</td>
    <td align="right">12.52</td>
    <td align="right">11.61</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">70.38</td>
    <td align="right">52.84</td>
    <td align="right">24.39</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">11.29</td>
    <td align="right">9.49</td>
    <td align="right">9.73</td>
    <td align="center">14</td>
    <td align="right">0.0153</td>
    <td align="right">20.16</td>
    <td align="right">17.27</td>
    <td align="right">17.43</td>
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
    <td align="right">3.17</td>
    <td align="right">4.55</td>
    <td align="right">3.62</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">2.49</td>
    <td align="right">3.42</td>
    <td align="right">2.59</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">3.58</td>
    <td align="right">3.84</td>
    <td align="right">3.15</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">2.69</td>
    <td align="right">7.02</td>
    <td align="right">5.06</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">5.70</td>
    <td align="right">6.34</td>
    <td align="right">6.09</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">8.34</td>
    <td align="right">9.40</td>
    <td align="right">9.00</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">12.31</td>
    <td align="right">11.51</td>
    <td align="right">8.86</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">9.36</td>
    <td align="right">7.40</td>
    <td align="right">8.48</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">15.05</td>
    <td align="right">12.37</td>
    <td align="right">11.73</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0276</td>
    <td align="right">11.99</td>
    <td align="right">13.85</td>
    <td align="right">9.86</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">8.83</td>
    <td align="right">8.03</td>
    <td align="right">8.19</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">20.46</td>
    <td align="right">15.97</td>
    <td align="right">17.71</td>
  </tr>
</table>

<!--clang-arm64/comparison_table.cpp.txt-->

### VS 2022, x64
<!--vs-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">35.61</td>
    <td align="right">6.08</td>
    <td align="right">3.87</td>
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
    <td align="right">12.16</td>
    <td align="right">12.42</td>
    <td align="right">16.97</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">5.82</td>
    <td align="right">4.47</td>
    <td align="right">4.39</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">7.85</td>
    <td align="right">5.98</td>
    <td align="right">6.03</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">18.23</td>
    <td align="right">17.55</td>
    <td align="right">17.58</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">6.91</td>
    <td align="right">5.01</td>
    <td align="right">5.07</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">11.57</td>
    <td align="right">8.43</td>
    <td align="right">8.51</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">23.45</td>
    <td align="right">21.34</td>
    <td align="right">16.69</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">8.66</td>
    <td align="right">5.64</td>
    <td align="right">5.51</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">15.52</td>
    <td align="right">14.14</td>
    <td align="right">12.95</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">31.00</td>
    <td align="right">26.70</td>
    <td align="right">17.13</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">9.92</td>
    <td align="right">6.28</td>
    <td align="right">6.38</td>
    <td align="center">14</td>
    <td align="right">0.0163</td>
    <td align="right">18.06</td>
    <td align="right">15.97</td>
    <td align="right">15.96</td>
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
    <td align="right">7.70</td>
    <td align="right">10.66</td>
    <td align="right">10.66</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">6.97</td>
    <td align="right">5.32</td>
    <td align="right">5.23</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">14.01</td>
    <td align="right">6.68</td>
    <td align="right">5.81</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5384</td>
    <td align="right">3.60</td>
    <td align="right">6.10</td>
    <td align="right">5.47</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">8.07</td>
    <td align="right">5.93</td>
    <td align="right">5.93</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">25.92</td>
    <td align="right">8.50</td>
    <td align="right">8.29</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1163</td>
    <td align="right">9.02</td>
    <td align="right">10.20</td>
    <td align="right">7.28</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">9.39</td>
    <td align="right">6.51</td>
    <td align="right">6.58</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">16.24</td>
    <td align="right">11.61</td>
    <td align="right">11.60</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0286</td>
    <td align="right">7.10</td>
    <td align="right">11.34</td>
    <td align="right">7.42</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">10.40</td>
    <td align="right">7.70</td>
    <td align="right">7.71</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">19.37</td>
    <td align="right">16.53</td>
    <td align="right">16.46</td>
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
    <td align="right">43.31</td>
    <td align="right">22.26</td>
    <td align="right">7.66</td>
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
    <td align="right">14.46</td>
    <td align="right">13.05</td>
    <td align="right">17.73</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">7.05</td>
    <td align="right">4.79</td>
    <td align="right">4.74</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">9.28</td>
    <td align="right">6.68</td>
    <td align="right">6.70</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">23.39</td>
    <td align="right">19.49</td>
    <td align="right">18.55</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">8.85</td>
    <td align="right">5.62</td>
    <td align="right">5.62</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">14.24</td>
    <td align="right">10.09</td>
    <td align="right">10.09</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">40.25</td>
    <td align="right">37.29</td>
    <td align="right">18.83</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">11.43</td>
    <td align="right">7.35</td>
    <td align="right">7.43</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">19.44</td>
    <td align="right">17.02</td>
    <td align="right">17.43</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">49.44</td>
    <td align="right">47.46</td>
    <td align="right">19.65</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">15.13</td>
    <td align="right">11.47</td>
    <td align="right">11.31</td>
    <td align="center">14</td>
    <td align="right">0.0153</td>
    <td align="right">23.97</td>
    <td align="right">23.55</td>
    <td align="right">24.08</td>
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
    <td align="right">7.84</td>
    <td align="right">10.71</td>
    <td align="right">10.72</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">7.87</td>
    <td align="right">5.64</td>
    <td align="right">5.68</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">14.14</td>
    <td align="right">6.07</td>
    <td align="right">6.16</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5394</td>
    <td align="right">5.70</td>
    <td align="right">8.32</td>
    <td align="right">7.55</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">10.38</td>
    <td align="right">7.41</td>
    <td align="right">7.40</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">26.70</td>
    <td align="right">9.31</td>
    <td align="right">9.32</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1161</td>
    <td align="right">11.62</td>
    <td align="right">12.72</td>
    <td align="right">9.66</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">12.54</td>
    <td align="right">9.29</td>
    <td align="right">9.38</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">20.73</td>
    <td align="right">15.43</td>
    <td align="right">15.45</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0287</td>
    <td align="right">13.72</td>
    <td align="right">18.12</td>
    <td align="right">13.38</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">14.83</td>
    <td align="right">11.72</td>
    <td align="right">11.30</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">25.77</td>
    <td align="right">22.66</td>
    <td align="right">23.09</td>
  </tr>
</table>

<!--vs-x64/comparison_table.cpp.txt-->
