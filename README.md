# Experimental results for [candidate Boost Bloom Library](https://github.com/joaquintides/bloom)

The tables show the false positive rate (FPR) and execution times in nanoseconds per operation 
for six different configurations of `boost::bloom::filter<int, ...>`
where `N` elements have been inserted. Filters are constructed with a capacity
`c*N` (bits), so `c` is the number of bits used per element. For each combination of `c` and
a given filter configuration, we have selected the optimum value of `K` (that yielding the minimum FPR).
Standard release-mode settings are used; 
AVX2 is indicated for Visual Studio builds (`/arch:AVX2`) and 64-bit GCC/Clang builds (`-mavx2`),
which causes `fast_multiblock32` to use its AVX2 variant.

For reference, we provide also insertion, successful lookup and unsuccessful lookup times
for a `boost::unordered_flat_set<int>` with the same number of elements `N`.

## Results

* [GCC 14, x64](#gcc-14-x64)
* [Clang 18, x64](#clang-18-x64)
* [Clang 15, ARM64](#clang-15-arm64)
* [VS 2022, x64](#vs-2022-x64)
* [GCC 14, x86](#gcc-14-x86)
* [Clang 18, x86](#clang-18-x86)
* [VS 2022, x86](#vs-2022-x86)

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
    <td align="right">27.17</td>
    <td align="right">4.37</td>
    <td align="right">3.89</td>
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
    <td align="right">11.61</td>
    <td align="right">11.49</td>
    <td align="right">16.95</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">4.13</td>
    <td align="right">4.24</td>
    <td align="right">4.34</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">6.03</td>
    <td align="right">5.79</td>
    <td align="right">5.79</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">18.36</td>
    <td align="right">15.54</td>
    <td align="right">17.49</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">4.94</td>
    <td align="right">4.94</td>
    <td align="right">4.92</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">7.05</td>
    <td align="right">8.87</td>
    <td align="right">8.87</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">21.78</td>
    <td align="right">18.59</td>
    <td align="right">16.56</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">5.47</td>
    <td align="right">5.38</td>
    <td align="right">5.51</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">10.27</td>
    <td align="right">14.02</td>
    <td align="right">13.91</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">27.37</td>
    <td align="right">23.93</td>
    <td align="right">16.90</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">6.23</td>
    <td align="right">6.14</td>
    <td align="right">6.00</td>
    <td align="center">14</td>
    <td align="right">0.0163</td>
    <td align="right">12.45</td>
    <td align="right">15.85</td>
    <td align="right">15.76</td>
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
    <td align="right">4.31</td>
    <td align="right">5.37</td>
    <td align="right">5.37</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">4.90</td>
    <td align="right">5.08</td>
    <td align="right">5.06</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">6.19</td>
    <td align="right">5.79</td>
    <td align="right">5.78</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5384</td>
    <td align="right">3.79</td>
    <td align="right">4.84</td>
    <td align="right">4.84</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">5.52</td>
    <td align="right">5.55</td>
    <td align="right">5.55</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">11.13</td>
    <td align="right">9.06</td>
    <td align="right">9.12</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1163</td>
    <td align="right">7.38</td>
    <td align="right">7.29</td>
    <td align="right">6.20</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">6.38</td>
    <td align="right">6.33</td>
    <td align="right">6.35</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">11.26</td>
    <td align="right">11.80</td>
    <td align="right">11.77</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0286</td>
    <td align="right">7.79</td>
    <td align="right">8.40</td>
    <td align="right">6.23</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">6.68</td>
    <td align="right">6.75</td>
    <td align="right">6.73</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">13.51</td>
    <td align="right">14.99</td>
    <td align="right">14.89</td>
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
    <td align="right">35.11</td>
    <td align="right">19.80</td>
    <td align="right">11.68</td>
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
    <td align="right">13.90</td>
    <td align="right">13.24</td>
    <td align="right">18.27</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">5.02</td>
    <td align="right">5.20</td>
    <td align="right">5.16</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">7.54</td>
    <td align="right">7.03</td>
    <td align="right">7.20</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">34.67</td>
    <td align="right">31.90</td>
    <td align="right">21.68</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">11.76</td>
    <td align="right">11.31</td>
    <td align="right">10.43</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">22.87</td>
    <td align="right">20.04</td>
    <td align="right">13.34</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">68.01</td>
    <td align="right">71.94</td>
    <td align="right">27.74</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">18.71</td>
    <td align="right">18.50</td>
    <td align="right">18.13</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">30.93</td>
    <td align="right">27.94</td>
    <td align="right">29.36</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">100.59</td>
    <td align="right">98.15</td>
    <td align="right">29.37</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">24.40</td>
    <td align="right">23.09</td>
    <td align="right">23.18</td>
    <td align="center">14</td>
    <td align="right">0.0153</td>
    <td align="right">46.88</td>
    <td align="right">43.02</td>
    <td align="right">41.05</td>
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
    <td align="right">5.55</td>
    <td align="right">7.06</td>
    <td align="right">7.22</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">6.08</td>
    <td align="right">6.39</td>
    <td align="right">6.75</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">8.60</td>
    <td align="right">6.88</td>
    <td align="right">7.74</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5394</td>
    <td align="right">9.93</td>
    <td align="right">10.26</td>
    <td align="right">10.54</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">11.79</td>
    <td align="right">12.20</td>
    <td align="right">9.95</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">28.02</td>
    <td align="right">25.74</td>
    <td align="right">20.13</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1161</td>
    <td align="right">28.53</td>
    <td align="right">25.08</td>
    <td align="right">20.52</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">19.92</td>
    <td align="right">22.27</td>
    <td align="right">17.65</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">25.87</td>
    <td align="right">31.92</td>
    <td align="right">35.96</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0287</td>
    <td align="right">31.97</td>
    <td align="right">31.96</td>
    <td align="right">18.84</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">26.31</td>
    <td align="right">23.97</td>
    <td align="right">22.99</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">42.45</td>
    <td align="right">40.92</td>
    <td align="right">40.61</td>
  </tr>
</table>

<!--gcc-x64/comparison_table.cpp.txt-->

### Clang 18, x64
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
    <td align="right">26.79</td>
    <td align="right">4.64</td>
    <td align="right">3.51</td>
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
    <td align="right">9.29</td>
    <td align="right">8.97</td>
    <td align="right">15.47</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">3.31</td>
    <td align="right">3.94</td>
    <td align="right">3.94</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">5.81</td>
    <td align="right">6.02</td>
    <td align="right">6.24</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">13.12</td>
    <td align="right">14.19</td>
    <td align="right">16.90</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">3.85</td>
    <td align="right">4.57</td>
    <td align="right">4.59</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">8.88</td>
    <td align="right">9.24</td>
    <td align="right">9.24</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">17.56</td>
    <td align="right">16.65</td>
    <td align="right">15.45</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">4.37</td>
    <td align="right">5.08</td>
    <td align="right">5.08</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">10.84</td>
    <td align="right">13.45</td>
    <td align="right">13.40</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">20.38</td>
    <td align="right">21.10</td>
    <td align="right">16.09</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">4.82</td>
    <td align="right">5.68</td>
    <td align="right">5.87</td>
    <td align="center">14</td>
    <td align="right">0.0163</td>
    <td align="right">14.29</td>
    <td align="right">13.82</td>
    <td align="right">13.87</td>
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
    <td align="right">3.58</td>
    <td align="right">3.98</td>
    <td align="right">3.98</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">3.87</td>
    <td align="right">4.59</td>
    <td align="right">4.56</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">5.07</td>
    <td align="right">6.20</td>
    <td align="right">5.87</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5384</td>
    <td align="right">2.93</td>
    <td align="right">3.71</td>
    <td align="right">3.71</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">4.50</td>
    <td align="right">5.34</td>
    <td align="right">5.33</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">7.58</td>
    <td align="right">9.12</td>
    <td align="right">9.10</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1163</td>
    <td align="right">5.45</td>
    <td align="right">5.95</td>
    <td align="right">4.45</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">4.93</td>
    <td align="right">6.00</td>
    <td align="right">6.00</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">10.04</td>
    <td align="right">14.01</td>
    <td align="right">13.97</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0286</td>
    <td align="right">6.27</td>
    <td align="right">6.93</td>
    <td align="right">4.47</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">5.41</td>
    <td align="right">6.58</td>
    <td align="right">6.45</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">14.69</td>
    <td align="right">15.31</td>
    <td align="right">15.34</td>
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
    <td align="right">17.39</td>
    <td align="right">6.49</td>
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
    <td align="right">10.59</td>
    <td align="right">9.90</td>
    <td align="right">15.97</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">3.60</td>
    <td align="right">4.28</td>
    <td align="right">4.28</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">6.60</td>
    <td align="right">6.75</td>
    <td align="right">7.11</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">14.61</td>
    <td align="right">14.85</td>
    <td align="right">17.14</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">4.79</td>
    <td align="right">4.78</td>
    <td align="right">4.77</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">9.56</td>
    <td align="right">9.67</td>
    <td align="right">9.67</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">19.09</td>
    <td align="right">20.72</td>
    <td align="right">16.39</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">6.04</td>
    <td align="right">5.87</td>
    <td align="right">6.24</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">12.34</td>
    <td align="right">15.48</td>
    <td align="right">16.50</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">49.41</td>
    <td align="right">51.57</td>
    <td align="right">20.11</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">13.21</td>
    <td align="right">14.63</td>
    <td align="right">14.74</td>
    <td align="center">14</td>
    <td align="right">0.0153</td>
    <td align="right">25.35</td>
    <td align="right">30.02</td>
    <td align="right">30.64</td>
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
    <td align="right">3.99</td>
    <td align="right">4.37</td>
    <td align="right">4.38</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">4.31</td>
    <td align="right">4.99</td>
    <td align="right">4.94</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">5.62</td>
    <td align="right">6.64</td>
    <td align="right">6.62</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5394</td>
    <td align="right">3.25</td>
    <td align="right">4.16</td>
    <td align="right">4.07</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">5.30</td>
    <td align="right">7.02</td>
    <td align="right">6.78</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">8.71</td>
    <td align="right">10.60</td>
    <td align="right">9.97</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1161</td>
    <td align="right">11.91</td>
    <td align="right">17.86</td>
    <td align="right">12.29</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">7.36</td>
    <td align="right">8.32</td>
    <td align="right">8.53</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">12.54</td>
    <td align="right">17.96</td>
    <td align="right">16.65</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0287</td>
    <td align="right">10.35</td>
    <td align="right">17.68</td>
    <td align="right">11.12</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">12.24</td>
    <td align="right">15.56</td>
    <td align="right">14.43</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">27.41</td>
    <td align="right">24.82</td>
    <td align="right">26.40</td>
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
    <td align="right">23.55</td>
    <td align="right">4.33</td>
    <td align="right">4.18</td>
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
    <td align="right">7.45</td>
    <td align="right">5.02</td>
    <td align="right">12.48</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">1.54</td>
    <td align="right">1.30</td>
    <td align="right">1.30</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">2.45</td>
    <td align="right">1.87</td>
    <td align="right">1.84</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">10.73</td>
    <td align="right">7.16</td>
    <td align="right">13.05</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">1.56</td>
    <td align="right">1.51</td>
    <td align="right">1.50</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.45</td>
    <td align="right">4.81</td>
    <td align="right">2.22</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">14.76</td>
    <td align="right">9.33</td>
    <td align="right">11.08</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">1.93</td>
    <td align="right">1.60</td>
    <td align="right">1.95</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">4.37</td>
    <td align="right">2.96</td>
    <td align="right">3.14</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">20.89</td>
    <td align="right">12.56</td>
    <td align="right">12.94</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">2.05</td>
    <td align="right">2.11</td>
    <td align="right">2.05</td>
    <td align="center">14</td>
    <td align="right">0.0163</td>
    <td align="right">5.20</td>
    <td align="right">4.20</td>
    <td align="right">3.68</td>
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
    <td align="right">2.20</td>
    <td align="right">1.87</td>
    <td align="right">1.85</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">1.66</td>
    <td align="right">1.39</td>
    <td align="right">1.40</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">2.43</td>
    <td align="right">1.91</td>
    <td align="right">1.90</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">1.66</td>
    <td align="right">1.52</td>
    <td align="right">1.69</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">2.24</td>
    <td align="right">1.52</td>
    <td align="right">1.56</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.61</td>
    <td align="right">2.56</td>
    <td align="right">2.45</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">3.42</td>
    <td align="right">2.74</td>
    <td align="right">2.27</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">2.94</td>
    <td align="right">2.14</td>
    <td align="right">1.88</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">4.70</td>
    <td align="right">3.45</td>
    <td align="right">3.74</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0304</td>
    <td align="right">4.25</td>
    <td align="right">3.75</td>
    <td align="right">2.31</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">2.56</td>
    <td align="right">1.93</td>
    <td align="right">2.07</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">5.53</td>
    <td align="right">5.11</td>
    <td align="right">5.65</td>
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
    <td align="right">32.41</td>
    <td align="right">20.04</td>
    <td align="right">13.75</td>
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
    <td align="right">17.26</td>
    <td align="right">16.89</td>
    <td align="right">25.83</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">4.49</td>
    <td align="right">4.32</td>
    <td align="right">4.75</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">3.94</td>
    <td align="right">4.07</td>
    <td align="right">5.40</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">28.06</td>
    <td align="right">26.67</td>
    <td align="right">22.93</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">6.14</td>
    <td align="right">4.72</td>
    <td align="right">6.88</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">7.26</td>
    <td align="right">8.38</td>
    <td align="right">4.84</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">51.01</td>
    <td align="right">43.58</td>
    <td align="right">23.10</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">10.19</td>
    <td align="right">8.52</td>
    <td align="right">8.40</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">16.21</td>
    <td align="right">13.49</td>
    <td align="right">14.83</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">69.78</td>
    <td align="right">50.41</td>
    <td align="right">24.74</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">11.73</td>
    <td align="right">9.99</td>
    <td align="right">9.73</td>
    <td align="center">14</td>
    <td align="right">0.0153</td>
    <td align="right">20.60</td>
    <td align="right">18.50</td>
    <td align="right">17.99</td>
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
    <td align="right">2.51</td>
    <td align="right">4.07</td>
    <td align="right">3.00</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">2.48</td>
    <td align="right">3.06</td>
    <td align="right">3.32</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">4.37</td>
    <td align="right">4.95</td>
    <td align="right">4.52</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">7.47</td>
    <td align="right">6.65</td>
    <td align="right">6.18</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">5.93</td>
    <td align="right">5.93</td>
    <td align="right">6.03</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">7.95</td>
    <td align="right">9.25</td>
    <td align="right">8.35</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">9.19</td>
    <td align="right">9.93</td>
    <td align="right">7.27</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">9.83</td>
    <td align="right">9.49</td>
    <td align="right">8.30</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">15.85</td>
    <td align="right">13.42</td>
    <td align="right">12.18</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0276</td>
    <td align="right">11.69</td>
    <td align="right">13.76</td>
    <td align="right">8.35</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">9.88</td>
    <td align="right">7.41</td>
    <td align="right">8.19</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">20.44</td>
    <td align="right">17.85</td>
    <td align="right">19.87</td>
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
    <td align="right">36.83</td>
    <td align="right">6.14</td>
    <td align="right">3.71</td>
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
    <td align="right">12.18</td>
    <td align="right">12.67</td>
    <td align="right">17.16</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">5.83</td>
    <td align="right">4.21</td>
    <td align="right">4.18</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">7.88</td>
    <td align="right">5.63</td>
    <td align="right">5.58</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">18.45</td>
    <td align="right">17.76</td>
    <td align="right">17.50</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">6.89</td>
    <td align="right">4.87</td>
    <td align="right">4.75</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">11.57</td>
    <td align="right">8.53</td>
    <td align="right">8.44</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">23.75</td>
    <td align="right">21.59</td>
    <td align="right">16.89</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">8.56</td>
    <td align="right">5.32</td>
    <td align="right">5.43</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">15.18</td>
    <td align="right">11.12</td>
    <td align="right">10.98</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">31.12</td>
    <td align="right">27.12</td>
    <td align="right">17.54</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">9.91</td>
    <td align="right">5.94</td>
    <td align="right">5.92</td>
    <td align="center">14</td>
    <td align="right">0.0163</td>
    <td align="right">18.09</td>
    <td align="right">14.39</td>
    <td align="right">14.25</td>
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
    <td align="right">3.39</td>
    <td align="right">3.96</td>
    <td align="right">3.92</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">7.03</td>
    <td align="right">5.27</td>
    <td align="right">5.37</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">9.11</td>
    <td align="right">5.70</td>
    <td align="right">5.67</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.89</td>
    <td align="right">4.86</td>
    <td align="right">4.07</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">8.03</td>
    <td align="right">6.11</td>
    <td align="right">5.92</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">16.54</td>
    <td align="right">8.80</td>
    <td align="right">8.00</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">5.02</td>
    <td align="right">7.14</td>
    <td align="right">5.48</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">9.34</td>
    <td align="right">6.95</td>
    <td align="right">6.74</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">16.89</td>
    <td align="right">10.57</td>
    <td align="right">10.50</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0304</td>
    <td align="right">5.13</td>
    <td align="right">7.14</td>
    <td align="right">5.37</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">10.56</td>
    <td align="right">7.45</td>
    <td align="right">7.47</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">19.41</td>
    <td align="right">12.95</td>
    <td align="right">13.73</td>
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
    <td align="right">47.58</td>
    <td align="right">22.88</td>
    <td align="right">10.63</td>
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
    <td align="right">14.62</td>
    <td align="right">13.25</td>
    <td align="right">17.74</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">7.06</td>
    <td align="right">4.50</td>
    <td align="right">4.60</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">9.41</td>
    <td align="right">6.37</td>
    <td align="right">6.30</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">22.95</td>
    <td align="right">19.53</td>
    <td align="right">18.70</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">9.29</td>
    <td align="right">5.35</td>
    <td align="right">5.64</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">15.57</td>
    <td align="right">10.85</td>
    <td align="right">10.56</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">35.13</td>
    <td align="right">37.66</td>
    <td align="right">20.01</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">14.99</td>
    <td align="right">9.29</td>
    <td align="right">9.89</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">33.62</td>
    <td align="right">24.67</td>
    <td align="right">26.31</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">89.93</td>
    <td align="right">85.97</td>
    <td align="right">25.04</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">21.93</td>
    <td align="right">19.97</td>
    <td align="right">20.49</td>
    <td align="center">14</td>
    <td align="right">0.0153</td>
    <td align="right">42.51</td>
    <td align="right">23.73</td>
    <td align="right">22.98</td>
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
    <td align="right">3.70</td>
    <td align="right">4.25</td>
    <td align="right">4.29</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">7.90</td>
    <td align="right">5.63</td>
    <td align="right">5.70</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">9.54</td>
    <td align="right">6.35</td>
    <td align="right">6.39</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">3.61</td>
    <td align="right">5.52</td>
    <td align="right">4.82</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">10.32</td>
    <td align="right">6.74</td>
    <td align="right">6.75</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">20.02</td>
    <td align="right">10.32</td>
    <td align="right">9.80</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">8.08</td>
    <td align="right">13.60</td>
    <td align="right">9.04</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">14.75</td>
    <td align="right">10.96</td>
    <td align="right">11.30</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">24.88</td>
    <td align="right">15.30</td>
    <td align="right">15.25</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0276</td>
    <td align="right">14.01</td>
    <td align="right">19.53</td>
    <td align="right">15.17</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">23.09</td>
    <td align="right">20.97</td>
    <td align="right">21.71</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">37.75</td>
    <td align="right">23.15</td>
    <td align="right">25.74</td>
  </tr>
</table>

<!--vs-x64/comparison_table.cpp.txt-->

### GCC 14, x86
<!--gcc-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">64.61</td>
    <td align="right">51.30</td>
    <td align="right">15.94</td>
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
    <td align="right">2.1546</td>
    <td align="right">27.14</td>
    <td align="right">41.38</td>
    <td align="right">35.67</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">12.56</td>
    <td align="right">15.96</td>
    <td align="right">15.99</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">16.26</td>
    <td align="right">20.59</td>
    <td align="right">20.54</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">37.20</td>
    <td align="right">64.10</td>
    <td align="right">39.24</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">17.36</td>
    <td align="right">19.50</td>
    <td align="right">19.30</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">21.46</td>
    <td align="right">26.90</td>
    <td align="right">26.79</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">45.09</td>
    <td align="right">78.27</td>
    <td align="right">38.32</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">17.40</td>
    <td align="right">18.65</td>
    <td align="right">18.53</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">29.09</td>
    <td align="right">33.23</td>
    <td align="right">33.23</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">57.19</td>
    <td align="right">97.45</td>
    <td align="right">37.60</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">18.26</td>
    <td align="right">18.88</td>
    <td align="right">18.86</td>
    <td align="center">14</td>
    <td align="right">0.0149</td>
    <td align="right">35.42</td>
    <td align="right">37.94</td>
    <td align="right">37.91</td>
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
    <td align="right">2.7635</td>
    <td align="right">10.64</td>
    <td align="right">13.91</td>
    <td align="right">13.67</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">16.18</td>
    <td align="right">19.78</td>
    <td align="right">19.75</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">30.70</td>
    <td align="right">22.28</td>
    <td align="right">22.28</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">12.89</td>
    <td align="right">16.66</td>
    <td align="right">16.08</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">16.16</td>
    <td align="right">18.66</td>
    <td align="right">18.69</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">39.93</td>
    <td align="right">29.09</td>
    <td align="right">29.03</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">14.56</td>
    <td align="right">19.58</td>
    <td align="right">19.52</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">18.20</td>
    <td align="right">18.70</td>
    <td align="right">18.36</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">64.24</td>
    <td align="right">46.07</td>
    <td align="right">46.04</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0297</td>
    <td align="right">24.20</td>
    <td align="right">25.76</td>
    <td align="right">25.71</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">19.04</td>
    <td align="right">20.05</td>
    <td align="right">20.14</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">78.09</td>
    <td align="right">55.67</td>
    <td align="right">55.73</td>
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
    <td align="right">96.54</td>
    <td align="right">119.74</td>
    <td align="right">30.22</td>
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
    <td align="right">2.1489</td>
    <td align="right">29.05</td>
    <td align="right">49.22</td>
    <td align="right">45.62</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">15.74</td>
    <td align="right">23.04</td>
    <td align="right">23.92</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">27.99</td>
    <td align="right">33.48</td>
    <td align="right">33.36</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">68.20</td>
    <td align="right">127.36</td>
    <td align="right">71.26</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">42.24</td>
    <td align="right">43.20</td>
    <td align="right">45.22</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">50.24</td>
    <td align="right">55.00</td>
    <td align="right">53.34</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">135.68</td>
    <td align="right">256.20</td>
    <td align="right">95.43</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">50.56</td>
    <td align="right">56.06</td>
    <td align="right">53.00</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">87.09</td>
    <td align="right">102.33</td>
    <td align="right">103.66</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">227.04</td>
    <td align="right">388.26</td>
    <td align="right">113.93</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">53.83</td>
    <td align="right">54.38</td>
    <td align="right">54.11</td>
    <td align="center">14</td>
    <td align="right">0.0158</td>
    <td align="right">98.18</td>
    <td align="right">109.46</td>
    <td align="right">111.22</td>
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
    <td align="right">2.7396</td>
    <td align="right">12.49</td>
    <td align="right">19.09</td>
    <td align="right">21.02</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">23.81</td>
    <td align="right">28.59</td>
    <td align="right">28.67</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">60.73</td>
    <td align="right">35.99</td>
    <td align="right">35.92</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">28.53</td>
    <td align="right">36.43</td>
    <td align="right">35.21</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">41.50</td>
    <td align="right">41.60</td>
    <td align="right">42.68</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">110.43</td>
    <td align="right">64.57</td>
    <td align="right">64.08</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">49.01</td>
    <td align="right">55.78</td>
    <td align="right">55.03</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">52.72</td>
    <td align="right">52.60</td>
    <td align="right">53.38</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">116.13</td>
    <td align="right">109.66</td>
    <td align="right">109.43</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0284</td>
    <td align="right">65.95</td>
    <td align="right">95.28</td>
    <td align="right">94.12</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">56.88</td>
    <td align="right">56.89</td>
    <td align="right">57.53</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">149.86</td>
    <td align="right">126.96</td>
    <td align="right">126.37</td>
  </tr>
</table>

<!--gcc-x86/comparison_table.cpp.txt-->

### Clang 18, x86
<!--clang-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">63.08</td>
    <td align="right">10.30</td>
    <td align="right">7.45</td>
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
    <td align="right">2.1546</td>
    <td align="right">13.80</td>
    <td align="right">22.74</td>
    <td align="right">26.69</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">9.54</td>
    <td align="right">12.44</td>
    <td align="right">12.44</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">12.79</td>
    <td align="right">16.02</td>
    <td align="right">16.07</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">19.70</td>
    <td align="right">35.17</td>
    <td align="right">29.18</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">12.22</td>
    <td align="right">14.15</td>
    <td align="right">14.16</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">17.34</td>
    <td align="right">22.44</td>
    <td align="right">22.59</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">25.17</td>
    <td align="right">47.33</td>
    <td align="right">29.93</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">13.73</td>
    <td align="right">15.39</td>
    <td align="right">15.50</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">24.02</td>
    <td align="right">32.27</td>
    <td align="right">32.23</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">32.70</td>
    <td align="right">60.48</td>
    <td align="right">30.41</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">14.55</td>
    <td align="right">16.37</td>
    <td align="right">16.36</td>
    <td align="center">14</td>
    <td align="right">0.0149</td>
    <td align="right">30.34</td>
    <td align="right">37.00</td>
    <td align="right">36.99</td>
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
    <td align="right">2.7635</td>
    <td align="right">7.02</td>
    <td align="right">9.50</td>
    <td align="right">9.39</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">11.78</td>
    <td align="right">13.91</td>
    <td align="right">13.89</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">13.30</td>
    <td align="right">16.74</td>
    <td align="right">16.77</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">11.27</td>
    <td align="right">14.01</td>
    <td align="right">13.97</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">13.51</td>
    <td align="right">15.42</td>
    <td align="right">15.39</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">17.85</td>
    <td align="right">22.37</td>
    <td align="right">22.34</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">13.65</td>
    <td align="right">17.54</td>
    <td align="right">17.53</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">14.66</td>
    <td align="right">16.83</td>
    <td align="right">16.79</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">25.64</td>
    <td align="right">30.93</td>
    <td align="right">30.94</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0297</td>
    <td align="right">17.10</td>
    <td align="right">21.94</td>
    <td align="right">22.07</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">16.00</td>
    <td align="right">17.92</td>
    <td align="right">17.89</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">33.14</td>
    <td align="right">35.89</td>
    <td align="right">35.77</td>
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
    <td align="right">97.82</td>
    <td align="right">54.97</td>
    <td align="right">20.54</td>
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
    <td align="right">2.1489</td>
    <td align="right">14.42</td>
    <td align="right">23.27</td>
    <td align="right">28.65</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">9.95</td>
    <td align="right">13.88</td>
    <td align="right">13.23</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">13.55</td>
    <td align="right">18.61</td>
    <td align="right">18.44</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">23.07</td>
    <td align="right">48.49</td>
    <td align="right">35.49</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">14.75</td>
    <td align="right">24.05</td>
    <td align="right">17.47</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">22.37</td>
    <td align="right">28.84</td>
    <td align="right">29.83</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">32.35</td>
    <td align="right">61.33</td>
    <td align="right">33.24</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">20.76</td>
    <td align="right">26.86</td>
    <td align="right">20.57</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">34.27</td>
    <td align="right">48.97</td>
    <td align="right">49.48</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">113.24</td>
    <td align="right">135.61</td>
    <td align="right">48.84</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">34.59</td>
    <td align="right">29.36</td>
    <td align="right">30.89</td>
    <td align="center">14</td>
    <td align="right">0.0158</td>
    <td align="right">71.08</td>
    <td align="right">69.21</td>
    <td align="right">67.24</td>
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
    <td align="right">2.7396</td>
    <td align="right">7.47</td>
    <td align="right">9.79</td>
    <td align="right">9.62</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">12.15</td>
    <td align="right">14.39</td>
    <td align="right">14.45</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">13.95</td>
    <td align="right">18.78</td>
    <td align="right">20.13</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">12.70</td>
    <td align="right">17.41</td>
    <td align="right">18.40</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">24.41</td>
    <td align="right">21.57</td>
    <td align="right">22.42</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">32.17</td>
    <td align="right">41.93</td>
    <td align="right">37.30</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">32.96</td>
    <td align="right">41.41</td>
    <td align="right">36.36</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">34.70</td>
    <td align="right">40.75</td>
    <td align="right">43.95</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">71.59</td>
    <td align="right">75.01</td>
    <td align="right">74.48</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0284</td>
    <td align="right">57.32</td>
    <td align="right">63.57</td>
    <td align="right">62.13</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">51.11</td>
    <td align="right">51.77</td>
    <td align="right">45.25</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">85.41</td>
    <td align="right">68.63</td>
    <td align="right">69.16</td>
  </tr>
</table>

<!--clang-x86/comparison_table.cpp.txt-->

### VS 2022, x86
<!--vs-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">43.09</td>
    <td align="right">8.95</td>
    <td align="right">6.68</td>
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
    <td align="right">2.1546</td>
    <td align="right">55.37</td>
    <td align="right">52.20</td>
    <td align="right">36.14</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">18.07</td>
    <td align="right">17.29</td>
    <td align="right">20.49</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">20.24</td>
    <td align="right">39.72</td>
    <td align="right">39.83</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">85.07</td>
    <td align="right">79.78</td>
    <td align="right">40.00</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">20.36</td>
    <td align="right">18.90</td>
    <td align="right">21.13</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">24.82</td>
    <td align="right">58.69</td>
    <td align="right">56.56</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">105.92</td>
    <td align="right">96.88</td>
    <td align="right">38.37</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">21.43</td>
    <td align="right">19.11</td>
    <td align="right">20.48</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">36.43</td>
    <td align="right">77.55</td>
    <td align="right">77.79</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">134.93</td>
    <td align="right">121.88</td>
    <td align="right">39.71</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">23.77</td>
    <td align="right">20.54</td>
    <td align="right">21.27</td>
    <td align="center">14</td>
    <td align="right">0.0149</td>
    <td align="right">41.93</td>
    <td align="right">92.64</td>
    <td align="right">92.91</td>
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
    <td align="right">2.7253</td>
    <td align="right">16.24</td>
    <td align="right">23.65</td>
    <td align="right">23.61</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">21.72</td>
    <td align="right">22.23</td>
    <td align="right">24.98</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">23.31</td>
    <td align="right">40.37</td>
    <td align="right">40.82</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5350</td>
    <td align="right">16.14</td>
    <td align="right">32.67</td>
    <td align="right">24.03</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">23.76</td>
    <td align="right">23.81</td>
    <td align="right">25.21</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">29.08</td>
    <td align="right">56.98</td>
    <td align="right">57.64</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1194</td>
    <td align="right">26.52</td>
    <td align="right">54.62</td>
    <td align="right">38.82</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">25.90</td>
    <td align="right">26.21</td>
    <td align="right">27.25</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">41.71</td>
    <td align="right">76.66</td>
    <td align="right">80.26</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0262</td>
    <td align="right">24.98</td>
    <td align="right">52.72</td>
    <td align="right">36.45</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">27.60</td>
    <td align="right">28.92</td>
    <td align="right">29.39</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">47.35</td>
    <td align="right">91.76</td>
    <td align="right">93.06</td>
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
    <td align="right">68.09</td>
    <td align="right">37.76</td>
    <td align="right">13.99</td>
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
    <td align="right">2.1489</td>
    <td align="right">63.64</td>
    <td align="right">57.04</td>
    <td align="right">40.68</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">23.65</td>
    <td align="right">18.06</td>
    <td align="right">22.43</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">25.17</td>
    <td align="right">40.94</td>
    <td align="right">45.98</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">97.70</td>
    <td align="right">89.83</td>
    <td align="right">45.65</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">38.02</td>
    <td align="right">22.66</td>
    <td align="right">24.97</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">47.64</td>
    <td align="right">64.61</td>
    <td align="right">77.31</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">176.14</td>
    <td align="right">137.71</td>
    <td align="right">51.59</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">47.24</td>
    <td align="right">27.32</td>
    <td align="right">30.91</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">47.44</td>
    <td align="right">99.43</td>
    <td align="right">98.86</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">400.11</td>
    <td align="right">350.03</td>
    <td align="right">90.18</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">65.71</td>
    <td align="right">40.52</td>
    <td align="right">40.27</td>
    <td align="center">14</td>
    <td align="right">0.0158</td>
    <td align="right">64.10</td>
    <td align="right">114.28</td>
    <td align="right">115.92</td>
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
    <td align="right">2.7254</td>
    <td align="right">19.92</td>
    <td align="right">32.36</td>
    <td align="right">35.79</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">25.89</td>
    <td align="right">25.99</td>
    <td align="right">28.78</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">30.86</td>
    <td align="right">45.79</td>
    <td align="right">50.76</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5375</td>
    <td align="right">20.13</td>
    <td align="right">49.62</td>
    <td align="right">39.14</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">37.51</td>
    <td align="right">35.58</td>
    <td align="right">35.14</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">40.69</td>
    <td align="right">71.16</td>
    <td align="right">70.12</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1187</td>
    <td align="right">42.57</td>
    <td align="right">90.03</td>
    <td align="right">72.46</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">42.73</td>
    <td align="right">47.58</td>
    <td align="right">33.01</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">46.99</td>
    <td align="right">80.48</td>
    <td align="right">83.60</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0287</td>
    <td align="right">38.57</td>
    <td align="right">89.90</td>
    <td align="right">84.55</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">65.80</td>
    <td align="right">72.10</td>
    <td align="right">90.58</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">73.05</td>
    <td align="right">124.20</td>
    <td align="right">137.58</td>
  </tr>
</table>

<!--vs-x86/comparison_table.cpp.txt-->
