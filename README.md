### GCC 14, x64
<!--gcc-x64/comparison_table.cpp.txt-->
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">35.85</td>
    <td align="right">21.40</td>
    <td align="right">9.03</td>
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
    <td align="right">12.73</td>
    <td align="right">17.57</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">4.92</td>
    <td align="right">5.20</td>
    <td align="right">5.21</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">7.24</td>
    <td align="right">7.31</td>
    <td align="right">7.06</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">25.88</td>
    <td align="right">21.21</td>
    <td align="right">19.64</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">10.31</td>
    <td align="right">11.90</td>
    <td align="right">10.41</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">13.02</td>
    <td align="right">13.63</td>
    <td align="right">13.41</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">49.25</td>
    <td align="right">45.23</td>
    <td align="right">23.37</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">16.77</td>
    <td align="right">17.68</td>
    <td align="right">15.53</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">24.06</td>
    <td align="right">23.07</td>
    <td align="right">28.57</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">95.56</td>
    <td align="right">91.23</td>
    <td align="right">27.42</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">20.79</td>
    <td align="right">20.84</td>
    <td align="right">18.21</td>
    <td align="center">14</td>
    <td align="right">0.0153</td>
    <td align="right">33.48</td>
    <td align="right">34.90</td>
    <td align="right">32.98</td>
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
    <td align="right">8.37</td>
    <td align="right">11.09</td>
    <td align="right">11.86</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">5.75</td>
    <td align="right">6.15</td>
    <td align="right">5.95</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">7.45</td>
    <td align="right">6.97</td>
    <td align="right">7.42</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5394</td>
    <td align="right">8.06</td>
    <td align="right">9.28</td>
    <td align="right">7.21</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">6.99</td>
    <td align="right">7.05</td>
    <td align="right">8.28</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">18.75</td>
    <td align="right">15.20</td>
    <td align="right">18.21</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1161</td>
    <td align="right">28.42</td>
    <td align="right">22.02</td>
    <td align="right">14.87</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">15.41</td>
    <td align="right">15.04</td>
    <td align="right">15.93</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">23.63</td>
    <td align="right">27.50</td>
    <td align="right">26.10</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0287</td>
    <td align="right">31.06</td>
    <td align="right">31.12</td>
    <td align="right">20.32</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">22.86</td>
    <td align="right">22.50</td>
    <td align="right">23.35</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">39.76</td>
    <td align="right">39.07</td>
    <td align="right">35.45</td>
  </tr>
</table>

<!--gcc-x64/comparison_table.cpp.txt-->

### Clang 18, X64
<!--clang-x64/comparison_table.cpp.txt-->
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">32.22</td>
    <td align="right">16.74</td>
    <td align="right">6.37</td>
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
    <td align="right">9.91</td>
    <td align="right">8.95</td>
    <td align="right">15.40</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">3.97</td>
    <td align="right">4.63</td>
    <td align="right">4.65</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">6.89</td>
    <td align="right">7.11</td>
    <td align="right">7.48</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">14.71</td>
    <td align="right">15.38</td>
    <td align="right">17.31</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">4.36</td>
    <td align="right">5.09</td>
    <td align="right">5.03</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">9.90</td>
    <td align="right">10.11</td>
    <td align="right">10.13</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">21.16</td>
    <td align="right">19.44</td>
    <td align="right">16.47</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">5.29</td>
    <td align="right">6.18</td>
    <td align="right">6.02</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">12.25</td>
    <td align="right">14.91</td>
    <td align="right">14.96</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">31.40</td>
    <td align="right">29.92</td>
    <td align="right">17.35</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">6.84</td>
    <td align="right">7.31</td>
    <td align="right">7.39</td>
    <td align="center">14</td>
    <td align="right">0.0153</td>
    <td align="right">16.21</td>
    <td align="right">16.15</td>
    <td align="right">16.80</td>
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
    <td align="right">4.24</td>
    <td align="right">4.98</td>
    <td align="right">4.97</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">4.62</td>
    <td align="right">5.33</td>
    <td align="right">5.34</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">5.95</td>
    <td align="right">7.03</td>
    <td align="right">7.03</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5394</td>
    <td align="right">3.33</td>
    <td align="right">4.22</td>
    <td align="right">4.22</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">5.07</td>
    <td align="right">5.96</td>
    <td align="right">5.84</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">8.33</td>
    <td align="right">10.50</td>
    <td align="right">10.54</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1161</td>
    <td align="right">11.08</td>
    <td align="right">7.74</td>
    <td align="right">6.42</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">6.15</td>
    <td align="right">7.06</td>
    <td align="right">7.25</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">12.44</td>
    <td align="right">16.07</td>
    <td align="right">14.51</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0287</td>
    <td align="right">10.63</td>
    <td align="right">10.34</td>
    <td align="right">7.36</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">7.64</td>
    <td align="right">9.01</td>
    <td align="right">8.98</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">17.64</td>
    <td align="right">18.56</td>
    <td align="right">18.30</td>
  </tr>
</table>

<!--clang-x64/comparison_table.cpp.txt-->

### Clang 15, ARM64
<!--clang-arm64/comparison_table.cpp.txt-->
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">28.38</td>
    <td align="right">13.16</td>
    <td align="right">8.08</td>
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
    <td align="right">8.46</td>
    <td align="right">8.62</td>
    <td align="right">17.29</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">3.06</td>
    <td align="right">3.92</td>
    <td align="right">4.01</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">3.68</td>
    <td align="right">3.56</td>
    <td align="right">4.17</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">20.99</td>
    <td align="right">20.18</td>
    <td align="right">22.62</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">8.33</td>
    <td align="right">6.50</td>
    <td align="right">6.10</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">5.54</td>
    <td align="right">9.24</td>
    <td align="right">7.11</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">46.97</td>
    <td align="right">36.54</td>
    <td align="right">23.74</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">9.34</td>
    <td align="right">8.51</td>
    <td align="right">8.51</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">15.06</td>
    <td align="right">13.26</td>
    <td align="right">12.62</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">73.26</td>
    <td align="right">54.18</td>
    <td align="right">24.59</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">12.07</td>
    <td align="right">9.65</td>
    <td align="right">9.80</td>
    <td align="center">14</td>
    <td align="right">0.0153</td>
    <td align="right">19.92</td>
    <td align="right">18.46</td>
    <td align="right">18.55</td>
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
    <td align="right">3.18</td>
    <td align="right">4.68</td>
    <td align="right">3.74</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">2.81</td>
    <td align="right">3.35</td>
    <td align="right">3.56</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">3.61</td>
    <td align="right">4.52</td>
    <td align="right">4.71</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">5.51</td>
    <td align="right">5.33</td>
    <td align="right">7.07</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">4.36</td>
    <td align="right">7.30</td>
    <td align="right">5.50</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">7.10</td>
    <td align="right">8.99</td>
    <td align="right">9.53</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">11.53</td>
    <td align="right">11.10</td>
    <td align="right">7.57</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">9.94</td>
    <td align="right">7.86</td>
    <td align="right">8.54</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">14.98</td>
    <td align="right">10.53</td>
    <td align="right">12.95</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0276</td>
    <td align="right">12.17</td>
    <td align="right">14.04</td>
    <td align="right">8.53</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">8.60</td>
    <td align="right">6.48</td>
    <td align="right">8.02</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">20.91</td>
    <td align="right">17.81</td>
    <td align="right">18.66</td>
  </tr>
</table>

<!--clang-arm64/comparison_table.cpp.txt-->
