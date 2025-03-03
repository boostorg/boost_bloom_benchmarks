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
    <td align="right">25.84</td>
    <td align="right">4.52</td>
    <td align="right">3.56</td>
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
    <td align="right">10.92</td>
    <td align="right">10.71</td>
    <td align="right">16.63</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">4.00</td>
    <td align="right">4.18</td>
    <td align="right">4.27</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">5.99</td>
    <td align="right">5.68</td>
    <td align="right">5.75</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">16.80</td>
    <td align="right">15.90</td>
    <td align="right">17.43</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">4.89</td>
    <td align="right">4.90</td>
    <td align="right">4.89</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">7.07</td>
    <td align="right">8.89</td>
    <td align="right">8.90</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">19.89</td>
    <td align="right">18.57</td>
    <td align="right">16.50</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">5.43</td>
    <td align="right">5.35</td>
    <td align="right">5.50</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">10.36</td>
    <td align="right">13.80</td>
    <td align="right">13.83</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">27.06</td>
    <td align="right">24.02</td>
    <td align="right">16.79</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">6.20</td>
    <td align="right">6.14</td>
    <td align="right">5.96</td>
    <td align="center">14</td>
    <td align="right">0.0163</td>
    <td align="right">12.36</td>
    <td align="right">15.92</td>
    <td align="right">15.89</td>
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
    <td align="right">7.97</td>
    <td align="right">10.62</td>
    <td align="right">10.74</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">4.88</td>
    <td align="right">5.07</td>
    <td align="right">5.05</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">6.15</td>
    <td align="right">5.68</td>
    <td align="right">5.74</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5384</td>
    <td align="right">3.74</td>
    <td align="right">4.79</td>
    <td align="right">4.78</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">5.48</td>
    <td align="right">5.87</td>
    <td align="right">5.52</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">11.71</td>
    <td align="right">9.08</td>
    <td align="right">9.07</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1163</td>
    <td align="right">17.14</td>
    <td align="right">10.47</td>
    <td align="right">8.27</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">6.23</td>
    <td align="right">6.29</td>
    <td align="right">6.29</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">11.26</td>
    <td align="right">11.74</td>
    <td align="right">11.75</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0286</td>
    <td align="right">9.07</td>
    <td align="right">10.57</td>
    <td align="right">6.14</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">6.71</td>
    <td align="right">6.68</td>
    <td align="right">6.74</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">13.52</td>
    <td align="right">14.65</td>
    <td align="right">14.66</td>
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
    <td align="right">29.00</td>
    <td align="right">16.49</td>
    <td align="right">6.33</td>
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
    <td align="right">13.70</td>
    <td align="right">12.67</td>
    <td align="right">17.57</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">4.75</td>
    <td align="right">4.93</td>
    <td align="right">5.02</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">7.09</td>
    <td align="right">6.84</td>
    <td align="right">6.86</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">19.68</td>
    <td align="right">18.41</td>
    <td align="right">18.09</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">5.50</td>
    <td align="right">5.51</td>
    <td align="right">5.54</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">7.93</td>
    <td align="right">9.75</td>
    <td align="right">9.72</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">25.55</td>
    <td align="right">23.37</td>
    <td align="right">17.52</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">6.79</td>
    <td align="right">6.34</td>
    <td align="right">7.00</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">12.13</td>
    <td align="right">15.01</td>
    <td align="right">15.07</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">38.63</td>
    <td align="right">36.89</td>
    <td align="right">18.47</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">7.92</td>
    <td align="right">8.18</td>
    <td align="right">8.92</td>
    <td align="center">14</td>
    <td align="right">0.0153</td>
    <td align="right">15.41</td>
    <td align="right">18.18</td>
    <td align="right">18.37</td>
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
    <td align="right">8.21</td>
    <td align="right">10.73</td>
    <td align="right">10.71</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">5.88</td>
    <td align="right">6.01</td>
    <td align="right">6.01</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">7.40</td>
    <td align="right">6.78</td>
    <td align="right">6.75</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5394</td>
    <td align="right">4.41</td>
    <td align="right">5.51</td>
    <td align="right">5.52</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">6.49</td>
    <td align="right">6.28</td>
    <td align="right">6.33</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">12.37</td>
    <td align="right">10.28</td>
    <td align="right">10.14</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1161</td>
    <td align="right">17.12</td>
    <td align="right">11.21</td>
    <td align="right">9.17</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">7.58</td>
    <td align="right">7.50</td>
    <td align="right">7.57</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">13.31</td>
    <td align="right">13.74</td>
    <td align="right">13.83</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0287</td>
    <td align="right">12.74</td>
    <td align="right">13.68</td>
    <td align="right">8.63</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">8.41</td>
    <td align="right">8.27</td>
    <td align="right">8.32</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">16.86</td>
    <td align="right">17.69</td>
    <td align="right">18.02</td>
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
    <td align="right">27.09</td>
    <td align="right">4.51</td>
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
    <td align="right">9.35</td>
    <td align="right">8.97</td>
    <td align="right">15.46</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">3.34</td>
    <td align="right">3.97</td>
    <td align="right">3.96</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">5.79</td>
    <td align="right">6.00</td>
    <td align="right">6.22</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">13.11</td>
    <td align="right">14.21</td>
    <td align="right">16.83</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">3.85</td>
    <td align="right">4.58</td>
    <td align="right">4.59</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">8.84</td>
    <td align="right">9.17</td>
    <td align="right">9.18</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">17.40</td>
    <td align="right">16.63</td>
    <td align="right">15.64</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">4.35</td>
    <td align="right">5.08</td>
    <td align="right">5.09</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">10.61</td>
    <td align="right">13.45</td>
    <td align="right">13.41</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">20.35</td>
    <td align="right">21.24</td>
    <td align="right">16.00</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">4.83</td>
    <td align="right">5.69</td>
    <td align="right">5.85</td>
    <td align="center">14</td>
    <td align="right">0.0163</td>
    <td align="right">14.20</td>
    <td align="right">13.83</td>
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
    <td align="right">3.50</td>
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
    <td align="right">5.86</td>
    <td align="right">5.88</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5384</td>
    <td align="right">2.89</td>
    <td align="right">3.70</td>
    <td align="right">3.70</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">4.48</td>
    <td align="right">5.50</td>
    <td align="right">5.28</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">7.57</td>
    <td align="right">9.31</td>
    <td align="right">9.28</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1163</td>
    <td align="right">10.66</td>
    <td align="right">6.30</td>
    <td align="right">4.80</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">4.94</td>
    <td align="right">5.98</td>
    <td align="right">5.99</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">10.82</td>
    <td align="right">13.90</td>
    <td align="right">12.83</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0286</td>
    <td align="right">6.08</td>
    <td align="right">6.87</td>
    <td align="right">4.53</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">5.43</td>
    <td align="right">6.40</td>
    <td align="right">6.43</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">14.91</td>
    <td align="right">15.32</td>
    <td align="right">15.33</td>
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
    <td align="right">33.92</td>
    <td align="right">20.06</td>
    <td align="right">6.85</td>
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
    <td align="right">11.20</td>
    <td align="right">10.73</td>
    <td align="right">16.40</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">3.96</td>
    <td align="right">4.62</td>
    <td align="right">4.61</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">6.96</td>
    <td align="right">7.23</td>
    <td align="right">7.57</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">15.18</td>
    <td align="right">15.84</td>
    <td align="right">17.46</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">4.54</td>
    <td align="right">5.09</td>
    <td align="right">5.12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">10.07</td>
    <td align="right">10.20</td>
    <td align="right">10.29</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">21.37</td>
    <td align="right">20.66</td>
    <td align="right">16.75</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">5.87</td>
    <td align="right">6.66</td>
    <td align="right">6.25</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">13.06</td>
    <td align="right">15.83</td>
    <td align="right">15.47</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">47.48</td>
    <td align="right">41.38</td>
    <td align="right">18.55</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">7.58</td>
    <td align="right">9.50</td>
    <td align="right">8.58</td>
    <td align="center">14</td>
    <td align="right">0.0153</td>
    <td align="right">17.71</td>
    <td align="right">17.57</td>
    <td align="right">18.00</td>
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
    <td align="right">4.41</td>
    <td align="right">5.15</td>
    <td align="right">5.10</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">4.66</td>
    <td align="right">5.39</td>
    <td align="right">5.44</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">6.05</td>
    <td align="right">7.10</td>
    <td align="right">7.11</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5394</td>
    <td align="right">3.62</td>
    <td align="right">4.91</td>
    <td align="right">4.70</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">5.62</td>
    <td align="right">6.15</td>
    <td align="right">6.19</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">8.53</td>
    <td align="right">11.14</td>
    <td align="right">11.21</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1161</td>
    <td align="right">13.26</td>
    <td align="right">8.50</td>
    <td align="right">9.43</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">6.80</td>
    <td align="right">12.31</td>
    <td align="right">14.67</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">16.06</td>
    <td align="right">19.74</td>
    <td align="right">19.85</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0287</td>
    <td align="right">18.79</td>
    <td align="right">24.24</td>
    <td align="right">15.27</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">15.99</td>
    <td align="right">16.01</td>
    <td align="right">15.86</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">31.88</td>
    <td align="right">29.11</td>
    <td align="right">38.05</td>
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
    <td align="right">27.82</td>
    <td align="right">9.79</td>
    <td align="right">5.31</td>
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
    <td align="right">9.21</td>
    <td align="right">6.31</td>
    <td align="right">14.45</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">1.64</td>
    <td align="right">2.97</td>
    <td align="right">1.62</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">4.16</td>
    <td align="right">2.08</td>
    <td align="right">2.00</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">13.01</td>
    <td align="right">7.72</td>
    <td align="right">18.92</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">1.55</td>
    <td align="right">1.51</td>
    <td align="right">1.47</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.65</td>
    <td align="right">3.04</td>
    <td align="right">2.50</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">15.06</td>
    <td align="right">9.49</td>
    <td align="right">12.46</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">1.97</td>
    <td align="right">1.79</td>
    <td align="right">1.80</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">4.55</td>
    <td align="right">3.65</td>
    <td align="right">3.35</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">20.05</td>
    <td align="right">12.32</td>
    <td align="right">12.89</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">2.65</td>
    <td align="right">2.42</td>
    <td align="right">2.32</td>
    <td align="center">14</td>
    <td align="right">0.0163</td>
    <td align="right">5.19</td>
    <td align="right">4.20</td>
    <td align="right">4.20</td>
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
    <td align="right">2.10</td>
    <td align="right">2.10</td>
    <td align="right">1.97</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">2.59</td>
    <td align="right">1.79</td>
    <td align="right">1.75</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">2.74</td>
    <td align="right">1.94</td>
    <td align="right">1.99</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">1.66</td>
    <td align="right">1.63</td>
    <td align="right">1.84</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">2.44</td>
    <td align="right">2.59</td>
    <td align="right">1.65</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.19</td>
    <td align="right">2.71</td>
    <td align="right">2.53</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">3.26</td>
    <td align="right">3.14</td>
    <td align="right">2.47</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">1.95</td>
    <td align="right">1.80</td>
    <td align="right">1.76</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">4.67</td>
    <td align="right">3.41</td>
    <td align="right">3.48</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0304</td>
    <td align="right">3.37</td>
    <td align="right">3.84</td>
    <td align="right">2.27</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">2.24</td>
    <td align="right">1.80</td>
    <td align="right">1.78</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">5.21</td>
    <td align="right">4.55</td>
    <td align="right">4.44</td>
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
    <td align="right">30.91</td>
    <td align="right">15.53</td>
    <td align="right">10.21</td>
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
    <td align="right">14.43</td>
    <td align="right">13.12</td>
    <td align="right">26.39</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">6.61</td>
    <td align="right">7.34</td>
    <td align="right">6.15</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">7.03</td>
    <td align="right">7.38</td>
    <td align="right">6.25</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">47.46</td>
    <td align="right">35.75</td>
    <td align="right">32.04</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">11.45</td>
    <td align="right">8.50</td>
    <td align="right">9.45</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">11.76</td>
    <td align="right">11.75</td>
    <td align="right">9.76</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">70.12</td>
    <td align="right">53.60</td>
    <td align="right">31.74</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">13.77</td>
    <td align="right">12.34</td>
    <td align="right">11.05</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">22.50</td>
    <td align="right">18.71</td>
    <td align="right">19.30</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">101.58</td>
    <td align="right">75.16</td>
    <td align="right">35.65</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">15.03</td>
    <td align="right">14.56</td>
    <td align="right">15.47</td>
    <td align="center">14</td>
    <td align="right">0.0153</td>
    <td align="right">30.22</td>
    <td align="right">27.48</td>
    <td align="right">28.72</td>
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
    <td align="right">6.19</td>
    <td align="right">9.30</td>
    <td align="right">9.21</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">4.45</td>
    <td align="right">5.23</td>
    <td align="right">5.46</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">5.15</td>
    <td align="right">7.25</td>
    <td align="right">5.84</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">9.91</td>
    <td align="right">12.48</td>
    <td align="right">13.68</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">10.89</td>
    <td align="right">9.77</td>
    <td align="right">9.76</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">12.76</td>
    <td align="right">11.98</td>
    <td align="right">10.92</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">16.91</td>
    <td align="right">17.82</td>
    <td align="right">12.13</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">13.25</td>
    <td align="right">10.52</td>
    <td align="right">9.44</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">18.98</td>
    <td align="right">14.75</td>
    <td align="right">14.96</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0276</td>
    <td align="right">16.27</td>
    <td align="right">15.74</td>
    <td align="right">10.11</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">8.88</td>
    <td align="right">7.68</td>
    <td align="right">7.10</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">22.00</td>
    <td align="right">19.62</td>
    <td align="right">16.62</td>
  </tr>
</table>

<!--clang-arm64/comparison_table.cpp.txt-->

### VS 2022, x64
<!--vs-x64/comparison_table.cpp.txt-->
<!--vs-x64/comparison_table.cpp.txt-->
